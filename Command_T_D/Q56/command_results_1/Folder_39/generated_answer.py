import re

def all_substring_of_size_n(s):
    m = re.findall('(.)\x01*', s)
    return list(set(m))