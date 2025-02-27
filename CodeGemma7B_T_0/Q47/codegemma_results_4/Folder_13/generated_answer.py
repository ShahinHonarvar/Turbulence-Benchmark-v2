import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = '(?<=.{12})([a-z]{57,60})(?=.{33})'
    return set(re.findall(pattern, text))