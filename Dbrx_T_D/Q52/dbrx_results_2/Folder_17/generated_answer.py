import re

def is_palindrome(string):
    string = string.lower()
    return string == string[::-1] and string.isalpha()

def palindrome_of_length_n(n, s):
    return {s[i:i + n] for i in range(len(s) - n + 1) if is_palindrome(s[i:i + n])}