from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letters += english_letters.upper()

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.lower() in english_letters))
        return s == s[::-1]

    def substrings(s):
        length = len(s)
        return (s[i:j] for i in range(length) for j in range(i + 5, min(length, i + 7) + 1))
    palindromes = set(filter(is_palindrome, substrings(s)))
    return palindromes