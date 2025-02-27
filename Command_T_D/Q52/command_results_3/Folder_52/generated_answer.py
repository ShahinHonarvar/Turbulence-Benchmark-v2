import re

def palindrome_of_length_n(text):
    return re.findall('[a-z]+', text.lower())