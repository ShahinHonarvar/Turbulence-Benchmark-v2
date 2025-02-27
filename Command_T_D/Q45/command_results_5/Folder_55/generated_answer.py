import re

def palindromes_between_indices(s):
    return set(re.findall('([A-Z]+)([a-z]+)([A-Z]+)', s))