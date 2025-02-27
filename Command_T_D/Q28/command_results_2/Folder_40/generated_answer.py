import re

def return_nth_smallest_ascii(s):
    x = re.findall('[a-z]', s)
    return sorted(x)[3]