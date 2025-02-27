import re

def return_n_smallest_chars(s):
    lst = re.findall('[A-Z]', s)
    return lst[:82]