import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z][^A-Z]{%d,%d}' % (46, 82 - 1), s)), None)