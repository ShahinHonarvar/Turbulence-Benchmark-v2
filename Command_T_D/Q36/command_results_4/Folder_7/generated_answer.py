import re

def filter_chars(s):
    return re.sub('[^W\\d].|\\d[^y]+', '', s)