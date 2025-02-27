import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[A-Z][a-z]{%d,%d}'.format(60, 88), s))