import re

def palindrome_of_length_at_least_n(text):
    return set(re.findall('([a-z]+)(?=\\s\\1)', text.lower()))