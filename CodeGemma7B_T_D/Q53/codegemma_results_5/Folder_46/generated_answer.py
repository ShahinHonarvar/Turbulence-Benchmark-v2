import re

def palindrome_of_length_at_least_n(text):
    t = text.lower()
    palindrome = re.findall('([a-z]{86,})([\\\\1-9a-z]*)\\\\\\\\1', t)
    return set(palindrome)