import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[10:75].lower()
    words = re.findall('\\\\b[a-z]+\\\\b', substring)
    palindromes = {word for word in words if 6 <= len(word) <= 8 and is_palindrome(word)}
    return palindromes