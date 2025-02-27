import re

def palindrome_of_length_n(text):
    return re.findall('[A-Z]+', text.lower())