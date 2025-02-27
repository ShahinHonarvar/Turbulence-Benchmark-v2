import re

def return_nth_smallest_ascii(s):
    ascii = re.findall('[a-z]', s)
    return sorted(ascii)[6]