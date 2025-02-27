import re

def return_n_smallest_chars(s):
    chars = re.findall('[A-Z]+', s)
    return sorted(chars[:46])