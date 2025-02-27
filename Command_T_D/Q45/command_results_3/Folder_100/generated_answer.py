import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[0:6:2], flags=re.I))