import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=.)(.)\\1', s[63:-1], flags=re.I))