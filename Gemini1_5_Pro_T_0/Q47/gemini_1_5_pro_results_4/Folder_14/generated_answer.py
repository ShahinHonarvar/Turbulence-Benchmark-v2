import re

def palindromes_of_specific_lengths(text):
    text = text[10:75].lower()
    return set([substring for substring in [text[i:j] for i in range(len(text)) for j in range(i, len(text) + 1)] if len(substring) in range(6, 9) and substring == substring[::-1] and re.match('^[a-z]+$', substring)])