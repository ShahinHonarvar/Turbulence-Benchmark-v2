import re

def palindrome_of_length_at_least_n(text):
    return {match.group(0) for match in re.finditer('[a-zA-Z]{32,}', text, re.IGNORECASE) if match.group(0) == match.group(0)[::-1]}