import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]{4,7}(?=[A-Z][a-z]{{4,7}})', s))