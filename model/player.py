import model.logger
import os

def dele(fpath):
    """
    删除文件
    :param fpath: 文件路径
    :return: 无
    """
    if os.path.exists(fpath):
        os.remove(fpath)

def doPlay(file,dell):
    cmd = ["play", str(file)]
    model.logger.moduleLoggerMain.info("Executing %s", " ".join(cmd))
    self.proc = subprocess.Popen(
        cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    if dell:
        dele(file)
    model.logger.moduleLoggerMain.info("play ok")

def playsound_from_file(file,dell=True):
    """
    播放音频文件
    :param file: 文件路径
    :return: 无
    """
    thread.start_new_thread(doPlay, (file,dell))