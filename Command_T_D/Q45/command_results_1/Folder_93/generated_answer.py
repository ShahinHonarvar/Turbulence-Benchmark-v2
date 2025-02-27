import re

def palindromes_between_indices(s):
    return set(map(str.lower, re.findall('(?<=.)([a-z])([a-z]{5})([a-z])\x01', s)))