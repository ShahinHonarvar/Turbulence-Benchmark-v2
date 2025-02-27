import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)([a-z]{5})\x01', s))