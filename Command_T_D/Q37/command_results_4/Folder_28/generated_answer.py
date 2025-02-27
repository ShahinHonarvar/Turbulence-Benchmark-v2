import re

def filter_chars(s):
    return re.sub('[^!~a-t]', '', s[20:80])