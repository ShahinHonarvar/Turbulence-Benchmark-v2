import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('[a-z]{1,112}(?=\\w{1,112})', s.lower()))