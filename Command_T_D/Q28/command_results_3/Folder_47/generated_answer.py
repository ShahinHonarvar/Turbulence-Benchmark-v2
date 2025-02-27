import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-z]', s[3:-1]) if ord(c) < ord(s[0])), s[0])