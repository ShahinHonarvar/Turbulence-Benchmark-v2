import re

def palindrome_of_length_n(s):
    return set(re.findall('((?:[A-Z0-9]+[A-Z0-9]?)[A-Z0-9]+)+[A-Z0-9]+', s, flags=re.I))