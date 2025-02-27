import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pattern = '(?<!\\\\.)(?<![a-z])[a-z]{4,}(?<![a-z])|(?<![a-z])[a-z]([a-z])\\\\2(?<![a-z])'
    return set(re.findall(pattern, text))