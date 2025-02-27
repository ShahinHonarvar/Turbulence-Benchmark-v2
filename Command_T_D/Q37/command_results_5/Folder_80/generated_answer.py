import re

def filter_chars(s):
    return re.sub('[a-i]{%d,%d}'.format(36, 79), '', s)