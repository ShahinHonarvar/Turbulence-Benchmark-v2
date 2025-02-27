import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = '(?i)([a-z]{52,56})'
    matches = re.findall(pattern, text[26:88])
    return set(matches)