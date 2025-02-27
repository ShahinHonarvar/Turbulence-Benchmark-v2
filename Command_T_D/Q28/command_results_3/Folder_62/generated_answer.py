import re

def return_nth_smallest_ascii(strng):
    res = re.sub('[a-z]{%d,%d}'.format(51, 78), '\\1', strng)
    return res[8]