import re

def filter_chars(s):
    return re.sub('[A-T]{%d,%d}'.format(10, 52), '', s)