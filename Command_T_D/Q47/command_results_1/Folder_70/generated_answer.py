import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]+'.lower(), text[10:70]))