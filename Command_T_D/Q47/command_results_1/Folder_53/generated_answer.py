import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]{3}[a-z]{2}){2}[a-z]{3})([a-z]{3}[a-z]{2}){2}[a-z]{3})', s[1:300]))