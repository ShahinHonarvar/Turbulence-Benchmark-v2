import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('(?i)([a-z]+)(?=.)([a-z]+)', text))