import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[a-z]{%d,%d}' % (8, 65), s), None)