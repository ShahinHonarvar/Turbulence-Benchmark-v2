import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('((?=([a-z]))[a-z]{55}(?=[a-z])))', s.lower()))