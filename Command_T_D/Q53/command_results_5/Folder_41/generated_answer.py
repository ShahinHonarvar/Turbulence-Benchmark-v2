import re

def palindrome_of_length_at_least_n(s):
    return re.findall('[a-z]+\\w{27}|([a-z]+\\w{27})([a-z]+)', s.lower())