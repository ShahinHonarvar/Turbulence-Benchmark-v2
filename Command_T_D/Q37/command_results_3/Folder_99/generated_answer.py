import re

def filter_chars(s):
    return re.sub('[^Th]{%d,%d}'.format(373, 901), '', s)