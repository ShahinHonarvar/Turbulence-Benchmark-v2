import re

def filter_chars(s):
    return re.sub('[A-b]{%d,%d}'.format(35, 98), '', s)