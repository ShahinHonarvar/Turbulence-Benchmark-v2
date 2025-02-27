import re

def palindromes_between_indices(text):
    return set(re.findall('[a-z]+', text[1:-1], flags=re.I))