import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\\\W+', '', s).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 47, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes