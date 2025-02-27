import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.findall('\\\\b[a-z]{59,}\\\\b', s)
    return {word for word in s if word == word[::-1]}