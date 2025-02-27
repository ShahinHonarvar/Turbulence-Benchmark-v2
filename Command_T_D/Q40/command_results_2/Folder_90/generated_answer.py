import re

def return_n_smallest_chars(s):
    m = re.findall('[A-Z]', s)
    return m[:24]