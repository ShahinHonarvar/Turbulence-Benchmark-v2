import re

def palindromes_between_indices(s):
    return re.findall('(?i)([a-z]+)\x01', s[4:-1])