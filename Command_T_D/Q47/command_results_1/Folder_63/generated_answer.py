import re

def palindromes_of_specific_lengths(str1):
    str1 = str1.lower()
    return set(re.findall('[a-z]{26,31}', str1[33:-33]))