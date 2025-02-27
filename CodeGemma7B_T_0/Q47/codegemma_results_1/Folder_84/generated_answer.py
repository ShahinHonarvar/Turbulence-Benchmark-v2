import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = '(?<=.{23})([a-z]{13,40})(?=\\\\.{77})'
    return set(re.findall(pattern, text))