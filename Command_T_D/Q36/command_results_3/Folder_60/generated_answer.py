import re

def filter_chars(s):
    return re.sub('[^a-z]{%d,%d}'.format(23, 83), '', s)