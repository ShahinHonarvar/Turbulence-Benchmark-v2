import re

def all_substring_of_size_n(s):
    if not s:
        return []
    return sorted(set(re.findall('(.)\x01*', s)))