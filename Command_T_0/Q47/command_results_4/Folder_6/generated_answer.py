import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+\\d{5}([a-z]+)', s[45:-3]))