import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)(^[a-z]{104,123}$)')
    return {word for word in re.findall(pattern, text[119:256])}