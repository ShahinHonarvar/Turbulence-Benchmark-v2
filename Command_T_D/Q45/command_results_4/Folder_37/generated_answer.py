import re

def palindromes_between_indices(s):
    res = set(re.findall('(?<=.)(.)\x01', s[1:-1]))
    return res