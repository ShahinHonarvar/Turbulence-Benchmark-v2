import re

def palindrome_of_length_n(str):
    return set(re.findall('[a-z]{39}', str.lower()))