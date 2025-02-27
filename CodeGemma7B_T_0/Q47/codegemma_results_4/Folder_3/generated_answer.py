import re

def palindromes_of_specific_lengths(text):
    """
    This function takes a string as input and returns a set of all palindromes
    of lengths between 49 and 51 (inclusive) in the substring from index 27 to
    index 95 (inclusive), both inclusive. The function is case-insensitive.
    """
    text = text.lower()
    pattern = re.compile('(?<=.{26})([a-z]{49,51})(?=.{69})')
    return {word for word in re.findall(pattern, text)}