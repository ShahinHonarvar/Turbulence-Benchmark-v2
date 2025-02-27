import re

def palindrome_of_length_n(text):
    if len(text) < 87:
        return set()
    return set(re.findall('((?i)(?:[a-z]){87}(?:[a-z]))', text))