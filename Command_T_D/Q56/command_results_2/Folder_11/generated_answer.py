import re

def all_substring_of_size_n(s):
    r = re.findall('(.)\x01*', s)
    return sorted(set(r))