import re

def palindromes_between_indices(s):
    return set(re.findall('((?i)[a-z]{3,})', s))