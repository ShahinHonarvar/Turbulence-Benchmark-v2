import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+', s[17:95], flags=re.I))