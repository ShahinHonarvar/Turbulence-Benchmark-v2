import re

def palindromes_of_specific_lengths(text):
    text = text[32:72].lower()
    return {text[i:i + length] for length in range(21, 33) for i in range(len(text) - length + 1) if text[i:i + length] == text[i:i + length][::-1] and re.match('^[a-z]+$', text[i:i + length])}