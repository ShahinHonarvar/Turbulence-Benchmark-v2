import re

def palindromes_of_specific_lengths(s):
    pattern = '(?i)[a-z]{10,50}'
    s = s[200:301]
    palindromes = set(re.findall(pattern, s))
    return palindromes