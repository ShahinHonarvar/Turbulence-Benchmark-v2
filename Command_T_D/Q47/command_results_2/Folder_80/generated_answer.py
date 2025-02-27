import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+'.lower(), s[35:88]))