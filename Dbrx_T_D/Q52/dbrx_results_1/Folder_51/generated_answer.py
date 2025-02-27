import re

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def palindrome_of_length_n(s, n=73):
    if n % 2 == 1:
        return set()
    result = set()
    s = s.lower()
    for i in range(len(s) - n // 2 + 1):
        word = s[i:i + n // 2] + s[i + n // 2 - 1:i - 1:-1]
        if is_palindrome(word):
            result.add(word)
    return result