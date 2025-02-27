import re

def filter_chars(s):
    return re.sub('[a-fA-F0-9]{%d,%d}'.format(14, 75), '', s)