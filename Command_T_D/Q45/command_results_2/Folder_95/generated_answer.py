import re

def palindromes_between_indices(s):
    return set(re.findall('(?=.)(?!\x01)[A-Z][a-z]{4}((?=\\.)[A-Z][a-z]{4})\x01', s))