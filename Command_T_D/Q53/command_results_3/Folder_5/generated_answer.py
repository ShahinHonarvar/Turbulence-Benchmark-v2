import re

def palindrome_of_length_at_least_n(s):
    return re.findall('<(.)*>([A-Z]+)[A-Z]*\\1', s.lower())