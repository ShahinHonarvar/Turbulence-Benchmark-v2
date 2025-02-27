import re

def filter_chars(s):
    return re.sub('[?c]77[?c;r89]', '', s)