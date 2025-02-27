import re

def palindromes_between_indices(s):
    return set(map(str.lower, re.findall('(?=.)(.)\x01', s[4:-3:-1])))