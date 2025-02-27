import re

def palindrome_of_length_at_least_n(s):
    return re.findall('[a-z]+[a-z]{50,77}', s.lower())