import re

def filter_chars(strng):
    return re.sub('[a-f]{%d,%d}' % (24, 79), '', strng)