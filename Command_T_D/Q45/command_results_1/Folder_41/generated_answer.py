import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]+[a-z]?)[a-z]+[a-z]?', s[2:-2], flags=re.I))