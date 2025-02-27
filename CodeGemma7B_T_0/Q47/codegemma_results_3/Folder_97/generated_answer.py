import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)([a-z]{38,49})', re.IGNORECASE)
    matches = pattern.finditer(text[28:95])
    return {match.group(1) for match in matches}