import re

def all_substring_of_size_n(s):
    res = re.findall('(\\w+\\w+\\w+)', s)
    return res