import re

def palindrome_of_length_n(text):
    text = text.lower()
    pattern = '(?=([' + '|'.join(re.findall('[a-zA-Z]', text)) + ']{48}))'
    return set(re.findall(pattern, text))