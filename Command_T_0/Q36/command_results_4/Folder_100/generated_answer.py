import re

def filter_chars(s):
    return re.sub('[A-z]{%d,%d}'.format(43, 69), '', s)