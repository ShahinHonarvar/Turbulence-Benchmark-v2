import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = 29
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes