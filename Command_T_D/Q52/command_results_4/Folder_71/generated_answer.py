import re

def palindrome_of_length_n(s):
    return re.findall('((?=.)(.)\\1)', s, flags=re.I)