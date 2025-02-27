import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = '(?<=.{22})([a-zA-Z]{17,55})(?=\\\\.{22})'
    return {word for word in re.findall(pattern, text)}