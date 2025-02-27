import re

def palindrome_of_length_at_least_n(text):
    return re.findall('[A-Z][a-z]{43}([A-Z][a-z]?)', text.lower())