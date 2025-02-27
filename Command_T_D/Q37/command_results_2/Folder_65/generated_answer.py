import re

def filter_chars(s):
    return re.sub('[0-9A-Z]{%d,%d}', '', s)