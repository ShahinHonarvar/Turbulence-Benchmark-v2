import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[A-Za-z]{93,}')
    return set(pattern.findall(s.lower()))