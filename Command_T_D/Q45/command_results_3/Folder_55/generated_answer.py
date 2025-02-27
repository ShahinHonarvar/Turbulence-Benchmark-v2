import re

def palindromes_between_indices(text):
    indices = range(0, 3)
    return re.findall('[a-z]+[a-z]+[a-z]+', text[indices[0]:indices[2]])