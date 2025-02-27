import re

def palindromes_between_indices(s):
    r = re.findall('[a-z]+', s[2:-2])
    return set(r)