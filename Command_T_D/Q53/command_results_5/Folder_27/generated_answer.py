import re

def palindrome_of_length_at_least_n(s):
    return re.findall('<(.)>(?=\\1)', s, flags=re.I)