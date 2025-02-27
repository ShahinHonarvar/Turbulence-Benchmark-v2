import re

def filter_chars(s):
    return re.sub('[^-v]{%221; 419}'.format(s), '', s)