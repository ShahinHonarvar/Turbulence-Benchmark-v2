import re

def palindromes_between_indices(s):
    s = s[0:9]
    if s.lower() == s.lower()[::-1]:
        return set([s])
    return set()