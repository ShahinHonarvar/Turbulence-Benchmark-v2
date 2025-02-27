import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]{3,60}[a-z]{3,60})\\1)', s[70:-70]))