import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    letters = re.findall('[a-z]', s)
    n = 52
    palindromes = {s[i:j + 1] for i in range(len(s)) for j in range(i + n - 1, len(s)) if s[i:j + 1] == s[i:j + 1][::-1]}
    return palindromes