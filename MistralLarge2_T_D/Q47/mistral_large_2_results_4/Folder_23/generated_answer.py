import re

def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    substring = text[23:95].lower()
    words = re.findall('\\\\b[a-z]+\\\\b', substring)
    palindromes = {word for word in words if 17 <= len(word) <= 55 and is_palindrome(word)}
    return palindromes