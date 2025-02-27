import re

def palindrome_of_length_n(s):
    return set(re.findall('(?i)([A-Z]|[a-z]){74}', s))