import re

def palindromes_between_indices(s):
    return set(re.findall('((?i)[a-z])\x01', s[2:-1]))