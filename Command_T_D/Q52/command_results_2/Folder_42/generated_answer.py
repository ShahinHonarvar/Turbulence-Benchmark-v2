import re

def palindrome_of_length_n(s):
    return re.findall('(?i)(?=([a-z]))\\1\\1'.format(279), s)