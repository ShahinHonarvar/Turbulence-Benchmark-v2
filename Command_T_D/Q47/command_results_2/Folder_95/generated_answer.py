import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('((?i)[a-z]+)([a-z]+)', s[12:56]))