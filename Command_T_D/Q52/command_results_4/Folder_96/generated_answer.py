import re

def palindrome_of_length_n(s):
    return re.findall('(?i)([a-z]+)(?=([a-z][a-z]+)$$)', s, flags=re.IGNORECASE)