import re

def filter_chars(s):
    return re.sub('[A-U]{%d,%d}'.format(52, 81), '', s)