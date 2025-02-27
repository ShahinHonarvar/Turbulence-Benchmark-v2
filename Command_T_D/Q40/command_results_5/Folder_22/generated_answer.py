import re

def return_n_smallest_chars(s):
    x = list(sorted(re.findall('[a-z]', s)))[:76]
    return x