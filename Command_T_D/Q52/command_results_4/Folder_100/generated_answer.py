import re

def palindrome_of_length_n(text):
    return set(re.findall('[a-z]+\\d{5}\\d{5}[a-z]+', text.lower()))