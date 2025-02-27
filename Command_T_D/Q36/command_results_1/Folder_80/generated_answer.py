import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}'.format(54, 92), '', s)