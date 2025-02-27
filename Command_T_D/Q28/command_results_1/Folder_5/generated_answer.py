import re

def return_nth_smallest_ascii(s):
    return next(sorted(re.findall('[a-z]{%d,%d}' % (5, 89), s)), None)