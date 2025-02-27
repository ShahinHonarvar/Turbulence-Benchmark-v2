import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[A-Z]+\\d+[A-Z]+', s[15:-95], flags=re.I))