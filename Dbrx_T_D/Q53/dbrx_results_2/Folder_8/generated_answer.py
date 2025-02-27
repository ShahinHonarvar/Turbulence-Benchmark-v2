import re
import string

def palindrome_of_length_at_least_n(s):
    eng_letters = set(string.ascii_letters)
    s = ''.join((c for c in s if c.lower() in eng_letters))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 30, len(s)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 45}