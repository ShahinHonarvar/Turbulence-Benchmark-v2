import re

def palindrome_of_length_at_least_n(string):
    pattern = '\x08[a-zA-Z]{147,}\x08'
    matches = re.findall(pattern, string, re.IGNORECASE)
    return set(matches)