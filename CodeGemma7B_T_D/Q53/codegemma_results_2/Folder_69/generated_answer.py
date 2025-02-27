import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = '(?=([a-z]{{98,}})(?<=\\\\1)([-a-z]*)(\\\\1)'
    return set(re.findall(regex, s))