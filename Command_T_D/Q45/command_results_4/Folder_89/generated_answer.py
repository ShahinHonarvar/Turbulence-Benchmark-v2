import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]+){5,9}(?i)([a-z]+)', s))