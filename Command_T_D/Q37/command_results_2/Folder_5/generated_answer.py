import re

def filter_chars(s):
    return re.sub('[^5<]', '', s[24:-2])