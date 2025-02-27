import re

def palindrome_of_length_n(string):
    pattern = re.compile('(?i)([a-z]{95})(?=[a-z]{95})')
    matches = pattern.findall(string)
    return set(matches)