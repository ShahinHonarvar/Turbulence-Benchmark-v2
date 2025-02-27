import re

def palindrome_of_length_n(s):
    if len(s) < 54:
        return set()
    return set(re.findall('[a-z]+'.lower(), s))