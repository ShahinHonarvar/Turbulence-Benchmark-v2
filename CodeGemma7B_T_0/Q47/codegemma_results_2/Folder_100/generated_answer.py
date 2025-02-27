import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = '(?<=.{29,96})([a-z]{12,18})(?=\\\\b)'
    return set(re.findall(pattern, text))