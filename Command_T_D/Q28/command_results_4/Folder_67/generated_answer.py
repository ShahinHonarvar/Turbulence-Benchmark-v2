import re

def return_nth_smallest_ascii(str):
    return next(re.findall('[a-z]{%d,%d}' % (60, 83), str), 'z')