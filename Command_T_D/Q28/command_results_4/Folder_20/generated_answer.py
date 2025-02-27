import re

def return_nth_smallest_ascii(s):
    ascii_list = re.findall('[A-Z]', s)
    ascii_list = sorted(set(ascii_list))
    return ascii_list[25]