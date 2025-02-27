import re

def palindrome_of_length_n(arg):
    result = set()
    pattern = re.compile('[a-zA-Z]{40}')
    for match in pattern.finditer(arg):
        if match.group().lower() == match.group().lower()[::-1]:
            result.add(match.group().lower())
    return result