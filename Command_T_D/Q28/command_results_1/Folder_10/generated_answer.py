import re

def return_nth_smallest_ascii(s):
    ascii = sorted(re.findall('[A-Z]{%d,%d}' % (38, 82), s))
    return ascii[19]