import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[119:257]
    words = re.findall('\\\\b[A-Za-z]+\\\\b', substring)
    palindromes = {word for word in words if is_palindrome(word) and 104 <= len(word) <= 123}
    return palindromes