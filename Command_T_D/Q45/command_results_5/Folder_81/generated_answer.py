import re

def palindromes_between_indices(text):
    res = set(re.findall('(?<=.)(.)\x01', text[0:6]))
    return res