import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 143):
        for j in range(i + 144, len(s), 144):
            palindrome = s[i:j]
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes