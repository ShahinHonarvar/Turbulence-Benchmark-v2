import re

def palindrome_of_length_n(str):
    return re.findall('[a-z]+\\d{5}\\1[a-z]+', str, flags=re.I)