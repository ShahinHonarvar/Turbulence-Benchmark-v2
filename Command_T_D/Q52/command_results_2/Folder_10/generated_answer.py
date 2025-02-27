import re

def palindrome_of_length_n(s):
    m = re.findall('[a-z]+', s.lower())
    return set(m + m[::-1])