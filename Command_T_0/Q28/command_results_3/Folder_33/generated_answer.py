import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z]{%22..{%74}', s) if ord(c) == 12))