import re

def palindrome_of_length_n(text):
    return re.findall('[a-z]+[a-z][^a-z]*[a-z]+[a-z]', text, flags=re.I)