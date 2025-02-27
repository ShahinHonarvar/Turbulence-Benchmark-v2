import re

def palindrome_of_length_n(s):
    return set(re.findall('(?=.)(.)\\1', s.lower()))