import re

def palindrome_of_length_n(s):
    return set(re.findall('(?i)(?=([a-z]){15}(?i)'.format(15), s))