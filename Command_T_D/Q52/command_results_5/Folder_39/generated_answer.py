import re

def palindrome_of_length_n(s):
    return re.findall('(?i)(?:[a-z]+\\w{58})\\w{58}([a-z]+)', s)