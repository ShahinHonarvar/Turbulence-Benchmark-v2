import re

def return_n_smallest_chars(s):
    m = re.findall('[a-z]', s)
    m.sort()
    return m[:28]