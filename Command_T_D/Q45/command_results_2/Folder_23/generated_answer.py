import re

def palindromes_between_indices(text):
    return set(re.findall('(?i)([a-z])\x01', text[:6]))