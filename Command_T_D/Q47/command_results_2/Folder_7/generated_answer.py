import re

def palindromes_of_specific_lengths(text):
    return re.findall('<(.)?)([a-z]+)([a-z]+)([a-z]?)>', text, flags=re.I)