from collections import defaultdict

def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    n = 94
    if len(s) < n:
        return palindromes
    for i in range(len(s) - n + 1):
        for j in range(i, i + n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
                break
    return palindromes