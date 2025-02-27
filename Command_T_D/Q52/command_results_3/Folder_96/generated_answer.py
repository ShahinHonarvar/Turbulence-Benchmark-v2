import re

def palindrome_of_length_n(s):
    return re.findall('[A-Z]+\\d+[A-Z]+', s.lower())