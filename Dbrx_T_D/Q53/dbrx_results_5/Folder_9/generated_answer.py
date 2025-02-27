import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 94):
        for j in range(i + 47, i + 95):
            if s[i:j + 1] == s[i:j + 1][::-1] and re.match('[a-z]', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if len(p) >= 95}