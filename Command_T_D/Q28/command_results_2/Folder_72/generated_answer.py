import re

def return_nth_smallest_ascii(s):
    return next((r for r in re.findall('[a-z]', s)))