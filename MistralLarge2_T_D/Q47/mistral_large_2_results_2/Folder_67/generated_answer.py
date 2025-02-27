import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[65:100]
    words = re.findall('\\\\b[a-z]+\\\\b', substring.lower())
    palindromes = {word for word in words if 26 <= len(word) <= 33 and is_palindrome(word)}
    return palindromes