import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+', s[40:90], flags=re.I))