import re

def palindrome_of_length_n(text):
    pattern = '(?i)[a-z]+'
    text = re.findall(pattern, text)
    return {word for word in set(text) if word == word[::-1] and len(word) == 445}