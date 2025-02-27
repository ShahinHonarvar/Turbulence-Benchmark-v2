import re

def palindrome_of_length_at_least_n(string):
    return set(filter(lambda word: len(word) >= 11, re.findall('[A-Za-z]+', string)))