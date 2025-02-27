import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?<=.{22})([a-z]{32,34})(?=\\\\.{22})')
    return {word for word in re.findall(pattern, text)}