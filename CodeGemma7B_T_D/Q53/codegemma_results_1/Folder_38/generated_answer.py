import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pattern = re.compile('(?P<palindrome>([a-z])\\\\2{55,})')
    matches = pattern.finditer(text)
    result = set()
    for match in matches:
        result.add(match.group('palindrome'))
    return result