import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]+)(?=\\W)'), s[1:-1])