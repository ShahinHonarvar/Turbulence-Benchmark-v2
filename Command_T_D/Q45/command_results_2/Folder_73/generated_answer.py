import re

def palindromes_between_indices(str):
    return re.findall('[a-z]+', str[3:6])