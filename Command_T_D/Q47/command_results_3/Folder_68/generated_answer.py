import re

def palindromes_of_specific_lengths(test_str):
    return set(re.findall('(?i)(?=([a-z]){50,100}(?i)([a-z]{50,100})', test_str))