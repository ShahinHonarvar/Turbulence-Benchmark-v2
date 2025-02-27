import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 16):
        for j in range(i + 8, len(s) - i + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]*', substring):
                palindromes.add(substring)
    return palindromes