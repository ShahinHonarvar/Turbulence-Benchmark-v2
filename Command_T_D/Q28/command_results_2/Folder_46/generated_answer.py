import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z][^A-Z]*', s[34:85]) if ord(c) < ord('U')))