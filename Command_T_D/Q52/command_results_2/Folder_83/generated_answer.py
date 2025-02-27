import re

def palindrome_of_length_n(s):
    return re.findall('[a-z]{24}', s.lower())