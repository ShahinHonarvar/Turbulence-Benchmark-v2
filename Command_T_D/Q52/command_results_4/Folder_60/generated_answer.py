import re

def palindrome_of_length_n(s):
    return re.findall('[a-z]+'.rstrip(), s.lower(), flags=re.I)