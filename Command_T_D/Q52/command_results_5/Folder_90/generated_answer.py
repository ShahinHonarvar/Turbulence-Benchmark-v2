import re

def palindrome_of_length_n(text):
    return set(re.findall('[a-z]{1,318}', text.lower()))