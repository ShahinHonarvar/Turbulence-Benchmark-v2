import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z]{%d,%d}' % (9, 22), s)), 'Z')