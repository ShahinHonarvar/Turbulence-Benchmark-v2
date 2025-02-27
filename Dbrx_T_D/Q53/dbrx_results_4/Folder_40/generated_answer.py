import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and re.match('\\b\\w\\w\\w\\b', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes