import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('(?i)(?=([a-z]{5,6}){5,6})[a-z]{5,6}(?=[a-z]{5,6}{5,6})', text[127:-2]))