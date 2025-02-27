import re

def palindromes_of_specific_lengths(str1):
    return re.findall('(?i)(?=([a-z]+\\d){8}[a-z]+\\d){8}(a-z)+\\d{8}(a-z)+)', str1[10:59])