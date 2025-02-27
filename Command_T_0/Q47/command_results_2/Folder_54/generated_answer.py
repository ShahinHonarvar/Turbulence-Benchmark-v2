import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{18,19}', s[27:-77]))