import re

def palindrome_of_length_n(text):
    return re.findall('[a-z]{223}264[a-z]{223}', text.lower())