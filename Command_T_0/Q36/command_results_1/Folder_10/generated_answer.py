import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}'.format(35, 60), '', s)