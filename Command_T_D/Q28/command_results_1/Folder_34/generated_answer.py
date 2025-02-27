import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[A-Z]{%d,%d}' % (0, 18), s), None)