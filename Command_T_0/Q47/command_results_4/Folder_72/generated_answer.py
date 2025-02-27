import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{27,58}(?=\\W|$)', s[26:-1]))