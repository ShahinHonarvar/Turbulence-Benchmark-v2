import re

def filter_chars(s):
    return re.sub('[^!~]{170,195}[^!~]', '', s)