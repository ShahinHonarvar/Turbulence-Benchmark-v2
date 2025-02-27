import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('(?<=\\d){19}(?<=\\d){55}(?<=\\d)', text.lower()))