import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('<(A-Z){5}(?=([A-Z]+[a-z]))', s[29:-29]))