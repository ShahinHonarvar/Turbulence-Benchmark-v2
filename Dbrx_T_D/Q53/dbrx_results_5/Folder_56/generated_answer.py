import re
import string

def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.lower() in string.ascii_letters))
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=84):
    return {palindrome for palindrome in set(re.findall(f'(?=([A-Za-z]{{n}}))[A-Za-z]*', s)) if is_palindrome(palindrome)}