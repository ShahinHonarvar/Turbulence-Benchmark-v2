import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+\\d+[a-z]+', s[0:7]))