import re

def return_nth_smallest_ascii(s):
    m = re.search('[A-Z][^A-Z]*[A-Z]{%d,%d}'.format(47, 80), s)
    return m.group()