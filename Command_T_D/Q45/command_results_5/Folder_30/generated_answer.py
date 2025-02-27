import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?:[a-z]{2,3})\x01', s[0:5]))