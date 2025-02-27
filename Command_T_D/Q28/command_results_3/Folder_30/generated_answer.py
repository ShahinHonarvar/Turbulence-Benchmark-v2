import re

def return_nth_smallest_ascii(s):
    return next(sorted(re.findall('[a-z]', s)[50:76])[10])