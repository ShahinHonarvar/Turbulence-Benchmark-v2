import re

def palindromes_between_indices(s):
    pat = re.compile('[a-z]+', flags=re.I)
    return set(pat.findall(s[2:-2]))