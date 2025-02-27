import re

def palindrome_of_length_n(s):
    return set(re.findall('[a-z]{29}', s.lower()))