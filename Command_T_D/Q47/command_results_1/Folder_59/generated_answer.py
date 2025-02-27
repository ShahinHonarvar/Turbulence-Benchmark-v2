import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]{3,15}', text[0:100].lower()))