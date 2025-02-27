import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[a-z]{%d,%d}' % (63, 76), s)))