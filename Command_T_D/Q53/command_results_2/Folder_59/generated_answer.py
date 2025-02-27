import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('(?=([a-z]){20}(?=[A-Z]))', s.lower()))