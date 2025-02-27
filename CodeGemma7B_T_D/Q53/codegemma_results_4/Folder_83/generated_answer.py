import re

def palindrome_of_length_at_least_n(s):
    regex = '(?i)([a-z])\\\\1{59,}'
    return set(re.findall(regex, s))