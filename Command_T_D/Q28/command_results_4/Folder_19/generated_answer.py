import re

def return_nth_smallest_ascii(s):
    str_ary = re.findall('[A-Z]', s)
    str_ary = sorted(str_ary)
    return str_ary[12]