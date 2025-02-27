import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([^aieou])\x01)+', s[3:-1]))