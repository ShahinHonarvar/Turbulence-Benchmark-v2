import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[a-zA-Z]{76,}', re.IGNORECASE)
    matches = pattern.findall(s)
    return set(filter(lambda x: x == x[::-1], matches))