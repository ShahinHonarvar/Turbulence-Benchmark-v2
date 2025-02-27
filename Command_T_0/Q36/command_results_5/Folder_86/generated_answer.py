import re

def filter_chars(s):
    return re.sub('[^X}]{672,709}', '', s)