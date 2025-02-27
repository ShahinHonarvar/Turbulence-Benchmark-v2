import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z][^A-Z]*', s) if ord(c) > 47 and ord(c) < 81))