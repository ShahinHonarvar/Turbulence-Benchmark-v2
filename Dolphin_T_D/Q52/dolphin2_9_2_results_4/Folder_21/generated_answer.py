import re

def palindrome_of_length_n(string):
    words = re.findall('[a-zA-Z]{407}', string)
    return set([word.lower() for word in words if word.lower() == word[::-1]])