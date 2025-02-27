import re

def palindromes_between_indices(s):
    m = re.findall('[a-z]{3}([a-z]+){5}([a-z]{3})', s.lower())
    return set(m)