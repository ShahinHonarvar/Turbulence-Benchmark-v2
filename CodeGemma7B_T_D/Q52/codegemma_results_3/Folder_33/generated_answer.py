import re

def palindrome_of_length_n(text):
    pattern = re.compile('(?i)([a-zA-Z]{475})')
    matches = re.findall(pattern, text)
    results = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            results.add(match)
    return results if results else set()