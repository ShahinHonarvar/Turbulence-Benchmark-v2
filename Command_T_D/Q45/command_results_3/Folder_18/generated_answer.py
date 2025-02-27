import re

def palindromes_between_indices(s):
    return re.findall('((?=.)(?!\x01)[a-z]{3}(?=\x01))', s)