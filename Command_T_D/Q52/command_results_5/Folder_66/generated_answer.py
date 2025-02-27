import re

def palindrome_of_length_n(s):
    return re.findall('[a-z]+', s.lower(), flags=re.I)[-25:]