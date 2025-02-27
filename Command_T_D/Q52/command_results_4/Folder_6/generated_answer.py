import re

def palindrome_of_length_n(s):
    return re.findall('([A-Z]+)([a-z]+)([A-Z]+)([a-z]+)', s.lower())