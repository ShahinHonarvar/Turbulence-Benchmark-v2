import re

def palindromes_of_specific_lengths(s):
    return re.findall('[A-Z]+[A-Z][^A-Z]+[A-Z]+[A-Z]', s[101:292])