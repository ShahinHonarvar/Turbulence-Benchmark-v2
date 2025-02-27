import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+' + '(?=([a-z]+){9})' + '([a-z]+){9}', s[10:-5]))