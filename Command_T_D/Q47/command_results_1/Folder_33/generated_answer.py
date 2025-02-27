import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)([a-z]+)([a-z]+)([a-z]+)([a-z]+)([a-z]+)', s[130:295], flags=re.I))