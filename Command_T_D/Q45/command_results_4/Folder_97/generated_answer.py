import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?<=.)(?=.)(.)\x01', s))