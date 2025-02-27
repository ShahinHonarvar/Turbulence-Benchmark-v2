import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?P<sub>.{3,8})\x01', s[3:-5], flags=re.I))