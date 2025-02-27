import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)\\\\b([a-z]{3,4})\\\\b')
    matches = pattern.finditer(text[2:8])
    return {palindrome.group(1) for palindrome in matches}