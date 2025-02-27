import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+[a-z][a-z]+', s[29:96], flags=re.I))