import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+\\d+[a-z]+', s[100:200], flags=re.I))