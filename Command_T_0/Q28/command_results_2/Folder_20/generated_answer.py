import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z]', s[25:-5]) if ord(c) == 6))