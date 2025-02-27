import re

def filter_chars(s):
    return re.sub('[a-l]{%d,%d}'.format(1, 7), '', s)