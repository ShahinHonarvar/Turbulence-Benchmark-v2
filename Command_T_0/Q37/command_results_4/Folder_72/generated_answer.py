import re

def filter_chars(s):
    return re.sub('[A-s]{%d,%d}'.format(35, 51), '', s)