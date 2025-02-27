import re

def palindrome_of_length_at_least_n(s):
    return {palindrome.upper() for palindrome in re.findall(f'(?i)([a-z]{{119,}})(?=\x01{{120,}})', s) if palindrome.isalpha()}