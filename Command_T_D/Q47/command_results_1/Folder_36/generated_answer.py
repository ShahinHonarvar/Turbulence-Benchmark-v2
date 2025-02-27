import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{115,134}{{-115,}}[a-z]{115,134}'.lower(), s[124:-12]))