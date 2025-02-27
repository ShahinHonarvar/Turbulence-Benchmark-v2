import re

def palindromes_between_indices(s):
    return re.findall('(\\w){6}(?=\\w\x01)', s[1:-1])