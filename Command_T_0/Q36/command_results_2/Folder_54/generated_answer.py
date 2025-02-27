import re

def filter_chars(s):
    return re.sub('[^A-Z]{%18,%38}', '', s)