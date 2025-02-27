import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]+', substring):
                if len(substring) >= 45:
                    palindromes.add(substring)
    return palindromes