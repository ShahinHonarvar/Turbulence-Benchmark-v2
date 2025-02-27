import re

def palindrome_of_length_at_least_n(n, text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) + 1):
            if len(text[i:j]) < n:
                continue
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes