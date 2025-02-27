import re

def palindromes_between_indices(s):
    letters = sorted((s[i] for i in range(min(8, len(s))) if s[i].isalpha()))
    return {palindrome for length in range(6, len(letters) + 1) for i in range(len(letters) - length + 1) for palindrome in {letters[i:i + length], letters[i:i + length][::-1]} if palindrome == palindrome.lower()}