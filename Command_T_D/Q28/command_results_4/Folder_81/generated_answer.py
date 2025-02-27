import re

def return_nth_smallest_ascii(s):
    return next(sorted(re.findall('[a-z]', s)), key=lambda x: ord(x))