import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{12,18}'.lower(), s[29:-29]))