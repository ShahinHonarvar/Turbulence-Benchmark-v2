import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 140 and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes