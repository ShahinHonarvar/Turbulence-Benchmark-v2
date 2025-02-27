import re

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    return set(re.findall('((?i)[a-z]+)\x01', s[2:9]))