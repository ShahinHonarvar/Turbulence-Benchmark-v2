import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[a-z]', s[3:-2]) if ord(c) == 8))