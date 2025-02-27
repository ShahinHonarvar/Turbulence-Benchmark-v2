import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]+', text[43:95], flags=re.I))