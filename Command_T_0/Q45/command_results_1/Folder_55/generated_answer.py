import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=.)(.)\\1', s[0:2]))