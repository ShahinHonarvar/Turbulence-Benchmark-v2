import re

def palindrome_of_length_at_least_n(text):
    return set(re.findall('[A-Z]+\\d+[A-Z]+', text.lower()))