import re

def filter_chars(s):
    return re.sub('[a-f]{%d,%d}'.format(24, 79), '', s)