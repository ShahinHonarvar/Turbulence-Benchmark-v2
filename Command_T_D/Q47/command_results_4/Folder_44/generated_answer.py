import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]+', text[18:98], flags=re.I))