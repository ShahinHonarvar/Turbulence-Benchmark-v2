import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]{10,50}(?=((?<=a-z)a-z){10,50}(?<=z))))', s[10:-10]))