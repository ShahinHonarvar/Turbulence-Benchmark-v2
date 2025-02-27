import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[a-z]{22,74}', s)[11])