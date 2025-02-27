import re

def filter_chars(s):
    return re.sub('[tT][a-fA-F0-9]{%d,%d}'.format(42, 68), '', s)