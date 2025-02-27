import re

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    return set(re.findall('((?=.)[a-z]+\x01)', s[1:-1]))