import re

def palindrome_of_length_n(s):
    return re.findall('[a-z]{34}', s.lower())