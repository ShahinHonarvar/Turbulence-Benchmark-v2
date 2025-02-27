import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return set(re.findall('\\\\b([a-z]{150,})\\\\b', s)) & set(re.findall('\\\\b([a-z]+)\\\\b', s))