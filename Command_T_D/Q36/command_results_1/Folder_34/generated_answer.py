import re

def filter_chars(s):
    return re.sub('[^?m]{%10,79}', '', s)