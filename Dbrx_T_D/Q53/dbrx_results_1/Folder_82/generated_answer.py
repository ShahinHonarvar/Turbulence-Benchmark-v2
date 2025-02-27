import re
import string

def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c in string.ascii_letters))
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=72):
    return {palindrome for palindrome in set(re.findall(f'.{n},.{n}', s)) if is_palindrome(palindrome)}