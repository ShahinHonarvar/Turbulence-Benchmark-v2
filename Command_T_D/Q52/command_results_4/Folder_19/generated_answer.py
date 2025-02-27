import re

def palindrome_of_length_n(s):
    return re.findall('[a-z]+', s, flags=re.I)[::-1]