import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=.*[a-z]){3}(?=.*[a-z]){4}(?=.*[a-z]){5}(?=.*[a-z])', s))