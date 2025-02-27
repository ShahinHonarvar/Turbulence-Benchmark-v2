import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[12:123].lower()
    words = re.findall('\\\\b[a-zA-Z]+\\\\b', substring)
    palindromes = {word for word in words if 12 <= len(word) <= 220 and is_palindrome(word)}
    return palindromes