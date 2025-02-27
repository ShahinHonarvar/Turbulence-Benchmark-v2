import re

def palindrome_of_length_n(text):
    return set(re.findall('[a-z]{38}', text.lower()))