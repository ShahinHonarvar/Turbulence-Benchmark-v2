import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('(?i)(?=([a-z]{11})))|([a-z]{11})', s))