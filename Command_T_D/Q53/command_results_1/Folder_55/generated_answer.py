import re

def palindrome_of_length_at_least_n(s):
    return set(map(str.lower, re.findall('((?i)[a-z]{84}(?i))', s)))