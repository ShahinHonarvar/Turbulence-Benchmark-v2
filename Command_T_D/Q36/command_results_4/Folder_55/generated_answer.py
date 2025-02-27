import re

def filter_chars(s):
    return re.sub('([^A-Z0-9])([A-Z]{%d,%d})([^A-Z0-9])'.format(3, 5), '\x01\x02\x03', s)