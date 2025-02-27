import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{103,158}'.lower(), s[130:-5]))