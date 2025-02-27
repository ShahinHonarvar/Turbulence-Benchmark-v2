import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=.*[a-z]){5,10}(?=.*[a-z]{100,200})', s))