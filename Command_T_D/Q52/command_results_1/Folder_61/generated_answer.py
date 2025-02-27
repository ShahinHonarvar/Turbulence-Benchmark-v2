import re

def palindrome_of_length_n(str):
    return re.findall('((?=.)[a-z]+\\Z)', str.lower())