import re

def palindrome_of_length_n(text):
    text = text.lower()
    regex = '(\\\\b[a-zA-Z]{49}\\\\b)'
    return {palindrome for palindrome in re.findall(regex, text)}