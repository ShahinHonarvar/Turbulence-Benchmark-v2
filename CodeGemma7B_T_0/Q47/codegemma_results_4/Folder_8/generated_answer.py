import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)([a-z]{50,51})', re.IGNORECASE)
    return {word for word in pattern.findall(text[16:72])}