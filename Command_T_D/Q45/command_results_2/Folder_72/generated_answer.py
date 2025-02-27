import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?P<l>[a-z])(?P<r>[a-z]){6}(?P<r>[a-z])(?P=l)', s[1:-1]))