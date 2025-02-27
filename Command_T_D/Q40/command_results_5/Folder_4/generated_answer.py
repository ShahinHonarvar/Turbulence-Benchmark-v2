import re

def return_n_smallest_chars(s):
    m = re.findall('[a-z]', s)
    return sorted(set(m), key=lambda x: ord(x))[:90]