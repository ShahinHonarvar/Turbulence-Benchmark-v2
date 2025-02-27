import re

def palindromes_between_indices(s):
    return set(re.findall('(?<=.)(.)\x01', s[2:-7:-1]))