import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[5:-2]) + re.findall('[a-z]+', s[6:-2]))