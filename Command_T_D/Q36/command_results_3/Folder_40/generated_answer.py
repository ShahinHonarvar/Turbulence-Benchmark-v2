import re

def filter_chars(s):
    return re.sub('[^-L]+', '', s, flags=re.I)