import re

def filter_chars(str):
    return re.sub('[^\\d~f]', '', str, flags=re.I)