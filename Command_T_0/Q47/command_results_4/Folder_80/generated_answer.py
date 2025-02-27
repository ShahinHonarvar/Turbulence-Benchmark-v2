import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{24,33}', s[35:-3]))