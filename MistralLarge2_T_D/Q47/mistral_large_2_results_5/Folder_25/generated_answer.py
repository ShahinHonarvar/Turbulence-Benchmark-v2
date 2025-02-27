import re

def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = string[26:85]
    words = re.findall('\\\\b[a-zA-Z]{30,46}\\\\b', substring)
    palindromes = {word.lower() for word in words if is_palindrome(word.lower())}
    return palindromes