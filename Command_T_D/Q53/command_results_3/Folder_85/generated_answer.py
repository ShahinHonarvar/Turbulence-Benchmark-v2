import re

def palindrome_of_length_at_least_n(text):
    return re.findall('[A-Za-z]+\\d+[A-Za-z]+', text.lower())