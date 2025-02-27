import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[a-z]', s[1:46]) if ord(c) == 13))