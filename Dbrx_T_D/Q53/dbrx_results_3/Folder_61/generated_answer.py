import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i, len(s) - i - 1):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes