import re

def filter_chars(s):
    return re.sub('[^*j]{%83,%99}', '', s)