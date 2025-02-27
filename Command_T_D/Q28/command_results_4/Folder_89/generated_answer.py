import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[a-z]', s[24:-1]), s[71])