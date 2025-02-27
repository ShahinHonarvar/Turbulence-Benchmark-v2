import re

def palindrome_of_length_n(s):
    return re.findall('[A-Z]+[A-Z][A-Z]+', s.lower())