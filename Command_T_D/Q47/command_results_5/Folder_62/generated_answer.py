import re

def palindromes_of_specific_lengths(str1):
    return set(re.findall('(?i)(?=.*[a-z])[a-z]+(?=.*[a-z])[a-z]+', str1[26:-87]))