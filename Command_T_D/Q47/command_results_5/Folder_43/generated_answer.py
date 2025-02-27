import re

def palindromes_of_specific_lengths(s):
    return re.findall('[a-z]+', s, flags=re.I)