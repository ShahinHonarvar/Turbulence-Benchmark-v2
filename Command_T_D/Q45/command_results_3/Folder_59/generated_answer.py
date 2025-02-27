import re

def palindromes_between_indices(text):
    return set(re.findall('(?<=.)(.)\x01', text[8:-9].lower()))