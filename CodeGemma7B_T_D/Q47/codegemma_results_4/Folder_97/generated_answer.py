import re

def palindromes_of_specific_lengths(text):
    text = text[28:95].lower()
    pattern = re.compile('\\\\b(\\\\w{38,49})\\\\b')
    return set((matches.group(1) for matches in pattern.finditer(text)))