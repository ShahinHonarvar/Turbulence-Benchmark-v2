import re

def palindromes_of_specific_lengths(text):
    pattern = '(?i)([a-zA-Z]{50,53})'
    matches = re.findall(pattern, text[31:92])
    return {match for match in matches}