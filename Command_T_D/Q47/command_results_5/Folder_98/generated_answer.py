import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('((?i)[a-z]+)(?i)(?=([a-z]+)[0-9]+)', s))