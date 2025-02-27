import re

def return_n_smallest_chars(s):
    m = re.findall('(.)', s)
    return m[:9]