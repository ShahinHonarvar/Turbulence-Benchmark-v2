import re
import string

def palindrome_of_length_at_least_n(s):
    english_letters = set(string.ascii_letters)
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(0, i - 83), i + 1):
            if s[i] in english_letters and s[i].lower() == s[j].lower():
                substring = ''.join((c for c in s[j:i + 1] if c in english_letters)).lower()
                if substring == substring[::-1] and len(substring) >= 84:
                    palindromes.add(substring)
    return palindromes