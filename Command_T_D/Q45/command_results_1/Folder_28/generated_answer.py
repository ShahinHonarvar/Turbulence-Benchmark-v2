import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=.*[a-z])[a-z]+(?=.*[a-z])', s[1:-1]))