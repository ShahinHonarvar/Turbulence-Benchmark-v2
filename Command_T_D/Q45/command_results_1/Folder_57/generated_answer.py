import re

def palindromes_between_indices(strng):
    strng = strng[2:-5]
    return set(re.findall('[a-z]+', strng.lower()))