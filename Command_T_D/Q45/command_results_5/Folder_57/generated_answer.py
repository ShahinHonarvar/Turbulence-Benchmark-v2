import re

def palindromes_between_indices(s):
    reg = '[a-z]+'
    return set(re.findall(f'(?=({reg})){reg}(?=({reg}))', s[2:-2]))