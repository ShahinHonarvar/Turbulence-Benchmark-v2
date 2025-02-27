import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]{3,15}))([a-z]{3,15})\\1', s[0:100]))