import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('[a-z]+\\d{2,}+[a-z]+', s.lower()))