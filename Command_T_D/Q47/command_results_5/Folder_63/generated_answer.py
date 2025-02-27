import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{26,31}(?=\\W|$)', s[33:-33], flags=re.I))