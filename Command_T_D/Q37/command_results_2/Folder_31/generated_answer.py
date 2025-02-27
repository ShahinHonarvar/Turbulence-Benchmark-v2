import re

def filter_chars(s):
    return re.sub('<(.)(w)+', '\x01', s)