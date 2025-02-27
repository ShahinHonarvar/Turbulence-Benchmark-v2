import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[A-Z]+\\d+[A-Z]+', s[124:283]))