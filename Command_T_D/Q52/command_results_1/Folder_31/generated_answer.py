import re

def palindrome_of_length_n(s):
    return set(re.findall('([a-z]+)(?i)([a-z]*)', s, flags=re.I))