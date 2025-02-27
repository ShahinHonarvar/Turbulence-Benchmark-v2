import re

def palindrome_of_length_n(s):
    return set(re.findall('[a-z]{100}'.lower(), s.lower()))