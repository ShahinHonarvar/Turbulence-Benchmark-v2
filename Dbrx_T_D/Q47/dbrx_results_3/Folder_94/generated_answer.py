import re

def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return c.lower().isalpha()

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(45, 52):
        for i in range(40, len(s) - length + 1):
            if is_english_letter(s[i]):
                palindrome_candidate = s[i:i + length]
                if is_palindrome(palindrome_candidate):
                    palindromes.add(palindrome_candidate)
    return palindromes