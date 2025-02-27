import re

def return_n_smallest_chars(s):
    res = sorted(re.findall('[a-z]', s))[:16]
    return res