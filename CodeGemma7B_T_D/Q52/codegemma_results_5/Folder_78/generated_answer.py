import re

def palindrome_of_length_n(text):
    text = text.lower()
    regex = '(?i)([a-z]{48})'
    result = set()
    for match in re.findall(regex, text):
        result.add(match)
    if not result:
        return set()
    return result