import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b[a-z]{149,}\\\\b', s)
    return {word for word in words if word == word[::-1]}