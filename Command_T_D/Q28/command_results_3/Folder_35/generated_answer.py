import re

def return_nth_smallest_ascii(s):
    m = re.match('<[A-Z]+>'.format(7), s)
    return m.group()