import re

def return_n_smallest_chars(s):
    return sorted(re.findall('[a-z]', s), key=lambda x: ord(x))[:43]