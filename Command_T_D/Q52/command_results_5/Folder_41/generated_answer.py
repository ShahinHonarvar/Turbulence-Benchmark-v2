import re

def palindrome_of_length_n(text):
    return set(re.findall('[a-z]+\\Z', text, flags=re.I))