import re

def return_nth_smallest_ascii(s):
    ascii_value = next(re.findall('[A-Z]', s[13:35]), -1)
    return chr(ascii_value)