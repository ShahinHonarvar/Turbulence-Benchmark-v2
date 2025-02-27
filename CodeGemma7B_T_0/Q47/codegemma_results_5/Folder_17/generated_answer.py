import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?<=.{22})(.*?)(?=\\\\.{95})', re.IGNORECASE)
    return {word for word in pattern.findall(text) if len(word) in range(52, 56)}