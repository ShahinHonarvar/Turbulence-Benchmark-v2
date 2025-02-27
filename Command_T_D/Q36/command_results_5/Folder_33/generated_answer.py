import re

def filter_chars(s):
    return re.sub('[^A-P]{%d,%d}'.format(299, 418), '', s)