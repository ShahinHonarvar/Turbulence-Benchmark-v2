import re

def palindrome_of_length_n(s):
    m = re.match('[a-z]{206}', s.lower())
    return set(m.group())