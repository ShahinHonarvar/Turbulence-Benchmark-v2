import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([^a-z]+15[^a-z]+89)).{40,72}(?=([^a-z]+15[^a-z]+89)))', s))