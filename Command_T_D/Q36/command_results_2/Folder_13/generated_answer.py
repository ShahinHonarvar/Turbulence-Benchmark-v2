import re

def filter_chars(s):
    return re.sub('(\\W)([A-Z]{%d%d})(\\W){%d%d}'.format(323, 526), '\x01\x03\x03\x02', s)