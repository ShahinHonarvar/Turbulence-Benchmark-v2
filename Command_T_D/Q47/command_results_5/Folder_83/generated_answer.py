import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{7,9}', s[75:-5]))