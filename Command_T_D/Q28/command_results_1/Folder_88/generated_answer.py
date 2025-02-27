import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-z]', s)[38:-6] if ord(c) == 14))