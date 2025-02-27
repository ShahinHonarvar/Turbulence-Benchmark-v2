import re

def palindromes_of_specific_lengths(text):
    text = text[119:257].lower()
    pattern = '[a-zA-Z]{104,123}'
    p = re.findall(pattern, text)
    return set(p)