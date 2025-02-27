import re

def palindromes_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 78, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes