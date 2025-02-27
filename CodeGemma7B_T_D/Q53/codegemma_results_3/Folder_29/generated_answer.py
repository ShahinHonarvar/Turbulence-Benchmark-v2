import re

def palindrome_of_length_at_least_n(text):
    pattern = re.compile('([a-zA-Z]{78,})')
    return set((match.group(1) for match in pattern.finditer(text)))