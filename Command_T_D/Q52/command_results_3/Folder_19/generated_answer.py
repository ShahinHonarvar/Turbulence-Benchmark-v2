import re

def palindrome_of_length_n(s):
    return set(re.findall('[a-z]{66}(?=\\w[a-z]{2})', s.lower()))