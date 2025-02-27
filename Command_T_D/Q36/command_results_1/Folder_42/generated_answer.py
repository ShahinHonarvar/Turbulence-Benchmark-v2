import re

def filter_chars(s):
    return re.sub('[^t<>]*([t<>])[^t<>]*', '\x01', s)