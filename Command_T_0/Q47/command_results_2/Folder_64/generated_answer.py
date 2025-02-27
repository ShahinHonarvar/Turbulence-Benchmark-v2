import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]{4,5}){4,5}(?i)([a-z]{4,5}){4,5})', s))