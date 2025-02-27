import re

def palindrome_of_length_at_least_n(s):
    words = re.findall('\\\\b[a-zA-Z]+\\\\b', s.lower())
    return {word for word in words if word == word[::-1] and len(word) >= 80}