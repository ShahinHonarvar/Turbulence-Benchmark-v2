import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?<=.{12})([a-z]{42,77})(?=.{92})')
    return set(pattern.findall(text))