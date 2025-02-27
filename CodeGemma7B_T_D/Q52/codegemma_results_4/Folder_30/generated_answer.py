import re

def palindrome_of_length_n(s):
    pattern = re.compile('[a-zA-Z]{94}')
    return set(pattern.findall(s, re.IGNORECASE))