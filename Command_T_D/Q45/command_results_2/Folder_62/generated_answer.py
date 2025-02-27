import re

def palindromes_between_indices(text):
    return set(re.findall('[a-z]+[a-z]{6,}', text[0:8]))