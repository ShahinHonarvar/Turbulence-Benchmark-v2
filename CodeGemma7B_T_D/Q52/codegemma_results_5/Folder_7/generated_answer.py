import re

def palindrome_of_length_n(text):
    n = 416
    text = text.lower()
    palindrome = set()
    pattern = '[a-z]{%d}' % n
    for match in re.finditer(pattern, text):
        palindrome.add(match.group(0))
    return palindrome