import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{50,51}', s[17:72]))