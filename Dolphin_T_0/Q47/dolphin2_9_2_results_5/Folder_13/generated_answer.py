import re

def palindromes_of_specific_lengths(s):
    substring = s[13:96]
    palindromes = set(re.findall('[a-zA-Z]{57,60}', substring))
    return palindromes