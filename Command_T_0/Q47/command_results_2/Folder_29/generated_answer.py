import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+\\d+[a-z]+', s[15:-15], flags=re.I))