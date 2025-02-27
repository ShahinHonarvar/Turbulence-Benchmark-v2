import re

def palindromes_of_specific_lengths(s):
    return re.findall('[a-z]{12,}\\d{5,}[a-z]{12}', s[12:-2])