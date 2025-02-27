import re

def palindrome_of_length_at_least_n(string):
    pattern = '(?i)(\\\\w{34,})'
    return set(re.findall(pattern, string))