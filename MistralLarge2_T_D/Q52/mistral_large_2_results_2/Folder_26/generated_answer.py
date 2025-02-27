import re

def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    substrings = [s[i:i + 366] for i in range(len(s) - 365)]
    palindromes = {substring for substring in substrings if is_palindrome(substring) and re.match('^[a-zA-Z]*$', substring)}
    return palindromes