import re

def palindrome_of_length_n(s):
    return re.findall('<(.*?)>', s.lower())