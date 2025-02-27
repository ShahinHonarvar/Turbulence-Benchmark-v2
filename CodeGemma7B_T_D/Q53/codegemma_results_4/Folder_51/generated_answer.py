import re

def palindrome_of_length_at_least_n(text):
    pattern = re.compile('(?i)(?:(?<![a-z])(?<![A-Z])([a-zA-Z]{63,})(?=[^a-z]|$)|([a-zA-Z]{63,})(?=[^a-z]|$))')
    return set(pattern.findall(text))