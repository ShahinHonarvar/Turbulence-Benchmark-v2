from collections import defaultdict

def is_english_letter(c):
    return c.lower().isalpha()

def longest_palindrome_substring(s):
    max_length = 1
    start = 0
    for i in range(1, len(s)):
        if i - max_length - 1 >= 0 and is_english_letter(s[i - max_length - 1]) and (s[i - max_length - 1] == s[i]):
            max_length += 2
            start = i - max_length
        elif i - max_length >= 0 and is_english_letter(s[i - max_length]) and (s[i - max_length] == s[i - 1]):
            max_length += 1
            start = i - max_length
    return s[start:start + max_length]

def palindrome_of_length_n(s, n):
    if n % 2 == 0:
        return set()
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if longest_palindrome_substring(substring) == substring:
            palindromes.add(substring)
    return palindromes