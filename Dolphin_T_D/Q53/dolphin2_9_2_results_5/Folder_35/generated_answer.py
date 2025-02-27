import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', '', s.lower())
    palindromes = set()
    for i in range(26, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes