import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('\\\\W+', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 57, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes