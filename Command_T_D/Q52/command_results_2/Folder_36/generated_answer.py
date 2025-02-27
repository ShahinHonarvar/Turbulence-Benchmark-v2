import re

def palindrome_of_length_n(text):
    return set(re.findall('((?i)(?=([a-z]+[a-z][a-z])))\\1', text))