import re

def palindrome_of_length_n(text):
    pattern = re.compile('[A-Za-z]{92}')
    return set((match.lower() for match in pattern.finditer(text)))