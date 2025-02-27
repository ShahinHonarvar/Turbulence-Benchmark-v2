import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]+\\d+[a-z]+', text[26:84]))