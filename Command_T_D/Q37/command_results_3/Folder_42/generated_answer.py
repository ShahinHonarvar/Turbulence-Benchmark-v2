import re

def filter_chars(s):
    return re.sub('[^A-Za-z]{%d,%d}'.format(73, 74), '', s)