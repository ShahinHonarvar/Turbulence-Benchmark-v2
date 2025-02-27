import re

def palindrome_of_length_n(s):
    return set(re.findall('[a-z]+'.zfill(18), s.lower()))