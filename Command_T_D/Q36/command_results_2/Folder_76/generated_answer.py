import re

def filter_chars(s):
    return re.sub('[^A-Z]{669,888}', '', s)