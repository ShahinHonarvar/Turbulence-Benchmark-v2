import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[A-Z][^A-Z]*[A-Z]', s[17:86]), '~')