import re

def return_nth_smallest_ascii(s):
    ascii_str = re.findall('[A-Z]', s)
    ascii_str.sort()
    return ascii_str[4]