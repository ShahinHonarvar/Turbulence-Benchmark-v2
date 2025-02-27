import re

def palindrome_of_length_at_least_n(string):
    palindrome = re.findall('(\\\\b[a-zA-Z]{45,})\\\\b', string, re.IGNORECASE)
    return set(palindrome) if palindrome else set()