import re

def filter_chars(s):
    return re.sub('[A-h]{%d,%d}'.format(24, 37), '', s)