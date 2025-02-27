import re

def palindrome_of_length_at_least_n(n, s):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    return set(filter(re.compile(pattern).fullmatch, s))