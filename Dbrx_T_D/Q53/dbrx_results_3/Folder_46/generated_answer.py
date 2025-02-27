import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(s[j:i:-1]) >= 86 and s[i:j + 1].lower() == s[j:i - 1:-1].lower() and re.fullmatch('[a-zA-Z]*', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes