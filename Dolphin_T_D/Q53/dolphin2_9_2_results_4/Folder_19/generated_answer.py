import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', '', s)
    s = s.lower()
    palindromes = set()
    for length in range(23, len(s) + 1):
        for i in range(len(s)):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes