import re

def return_nth_smallest_ascii(s):
    idx = re.findall('[a-z]', s)[-16]
    return s[idx]