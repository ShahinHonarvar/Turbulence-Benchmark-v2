import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('([a-zA-Z]{37,60})', re.IGNORECASE)
    matches = pattern.findall(text[11:84])
    return set(matches)