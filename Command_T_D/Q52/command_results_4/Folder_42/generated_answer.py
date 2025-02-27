import re

def palindrome_of_length_n(string):
    return re.findall('[a-z]+', string.lower(), flags=re.I)