import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]{2,4})\x01', s[3:-3]))