import re

def palindromes_between_indices(str):
    letters = list(re.findall('[a-z]+', str[1:-1]))
    return set(re.findall('|'.join((f'({s})' for s in letters)), str))