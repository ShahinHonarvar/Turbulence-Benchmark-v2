import re

def palindrome_of_length_n(text):
    """Functions that takes in a text and returns the unique palindromes that consist of english
    letters formed by the characters in the given text. Only palindromes of lenght 64 are 
    considered."""
    pattern = '[A-Za-z]{64}'
    matches = re.findall(pattern, text)
    return set(matches)