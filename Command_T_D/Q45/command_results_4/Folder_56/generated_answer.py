import re

def palindromes_between_indices(s):
    return set(re.findall('((?i)([a-z])\x01\x02\x03\x04\x05\x06\x07\\8\\9)', s[5:-4:-1]))