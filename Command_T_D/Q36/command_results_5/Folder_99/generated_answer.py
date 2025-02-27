import re

def filter_chars(str):
    return re.sub('[^b].*[^d]', '', str, flags=re.I)