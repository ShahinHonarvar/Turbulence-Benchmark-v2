import re

def palindromes_between_indices(str):
    s = list(str)
    return set(re.findall('([a-z]+)([A-Z][a-z]?)([a-z]?)\x01', s[5:-2:-2]))