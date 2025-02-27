import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+\\d+\\d+[a-z]+', s[62:-2]) + re.findall('[a-z]+\\d+[a-z]+\\d+', s[62:-2]))