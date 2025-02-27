import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-zA-Z]{16,39}', text[16:61]))