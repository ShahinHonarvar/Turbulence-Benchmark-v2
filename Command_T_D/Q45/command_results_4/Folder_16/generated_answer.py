import re

def palindromes_between_indices(s):
    return re.findall('[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', s[6:-2])