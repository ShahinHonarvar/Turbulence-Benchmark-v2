import re

def palindrome_of_length_at_least_n(s):
    return {palindrome.upper() for palindrome in find_long_palindromes(s) if len(palindrome) >= 100}

def find_long_palindromes(s):
    return {substring for substring in find_all_substrings(s) if is_palindrome(substring)}

def find_all_substrings(s):
    return re.findall('\\b[a-zA-Z]{100,}\\b', s)

def is_palindrome(s):
    return s == s[::-1]