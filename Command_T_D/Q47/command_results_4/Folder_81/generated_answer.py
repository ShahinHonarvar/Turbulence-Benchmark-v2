import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{12,220}'.lower(), s[12:-12]))