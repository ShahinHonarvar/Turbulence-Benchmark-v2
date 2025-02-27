import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.findall('\\\\b[a-z]{52,}\\\\b', s)
    return set(filter(lambda x: x == x[::-1], s))