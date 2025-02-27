import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 83 + 1):
        for j in range(i + 41, len(s)):
            current_substring = s[i:j + 1]
            if current_substring == current_substring[::-1] and re.fullmatch('[a-z]', current_substring):
                palindromes.add(current_substring)
    return palindromes