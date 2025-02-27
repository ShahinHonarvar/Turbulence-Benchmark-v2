import re

def palindromes_between_indices(str1):
    return set(re.findall('(?i)(?=.*?[a-z])[a-z]+(?=.*?[a-z])', str1[2:-2]))