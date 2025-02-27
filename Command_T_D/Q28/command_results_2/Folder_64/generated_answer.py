import re

def return_nth_smallest_ascii(s):
    return re.findall('[a-z]', s)[-6]