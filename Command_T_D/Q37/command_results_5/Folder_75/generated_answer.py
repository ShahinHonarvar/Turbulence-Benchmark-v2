import re

def filter_chars(s):
    return re.sub('[A-W][^x]{%d,%d}'.format(34, 67), '', s)