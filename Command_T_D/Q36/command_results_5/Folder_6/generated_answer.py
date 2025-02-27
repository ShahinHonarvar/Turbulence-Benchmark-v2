import re

def filter_chars(s):
    return re.sub('[A-Za-z]{%d,%d}'.format(31, 70), '', s)