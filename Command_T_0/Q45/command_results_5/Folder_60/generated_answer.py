import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([a-z]){3})([a-z]){4}(?=([a-z]){3})', s))