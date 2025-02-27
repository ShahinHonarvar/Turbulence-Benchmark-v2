import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=.*?[a-z])[a-z]+\x01', s[0:7]))