import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[3:-6], flags=re.I))