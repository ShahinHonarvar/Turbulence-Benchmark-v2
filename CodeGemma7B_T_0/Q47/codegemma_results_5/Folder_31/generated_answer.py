import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?<=.)(?<![a-z])([a-z]{37,60})(?<![a-z])(?=.)')
    return {word for word in re.findall(pattern, text[11:83])}