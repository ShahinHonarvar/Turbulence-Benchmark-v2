import re

def palindrome_of_length_n(s):
    return set(re.findall('(?i)(?=.)(.)\\1'.format(len(s)), s))