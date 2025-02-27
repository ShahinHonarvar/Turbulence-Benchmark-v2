import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]+)([a-z]?)\x01', s[5:-6]))