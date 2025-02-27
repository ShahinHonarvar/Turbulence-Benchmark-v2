import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{27}')
    return {word.lower() for word in pattern.findall(string)}