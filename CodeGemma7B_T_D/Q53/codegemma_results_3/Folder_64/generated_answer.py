import re

def palindrome_of_length_at_least_n(string):
    pattern = '([a-zA-Z])\\\\1{8,}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    return {match.lower() for match in matches if len(match) >= 9}