import re

def palindromes_of_specific_lengths(str):
    return set(re.findall('[a-z]{27,58}(?i)(?=\\W|$)', str[26:-1]))