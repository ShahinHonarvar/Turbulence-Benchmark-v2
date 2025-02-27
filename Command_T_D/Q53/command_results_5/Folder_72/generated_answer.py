import re

def palindrome_of_length_at_least_n(text):
    return set(re.findall('[a-z]{88,}(?=([a-z]{88}(?:[a-z]{1}){88})', text.lower()))