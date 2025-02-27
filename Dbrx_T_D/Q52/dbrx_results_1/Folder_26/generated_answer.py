import re

def palindrome_of_length_n(string):
    english_letters = set(re.findall('[a-z]', string.lower()))
    return {substr for substr in english_letters if substr * 366 in english_letters}