import re

def palindromes_of_specific_lengths(s):
    return set(map(str.lower, re.findall('(?=.*[a-z])[a-z]+(?=.*[a-z])', s[3:-3])))