import re

def return_nth_smallest_ascii(s):
    m = re.findall('[A-Z]{%d,%d}' % (28, 67), s)
    return sorted(m)[14]