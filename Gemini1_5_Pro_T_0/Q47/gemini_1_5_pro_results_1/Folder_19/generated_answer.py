import re

def palindromes_of_specific_lengths(text):
    text = text[10:56].lower()
    return {word for word in [text[i:j] for i in range(len(text)) for j in range(i, len(text) + 1)] if len(word) in range(3, 8) and word == word[::-1] and re.match('^[a-z]+$', word)}