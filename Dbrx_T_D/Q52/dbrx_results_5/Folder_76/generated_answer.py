from collections import defaultdict

def palindrome_of_length_n(s):
    n = 257
    if len(s) < n:
        return set()
    s = s.lower()
    odds = defaultdict(int)
    palindromes = set()
    for i in range(len(s) - n + 1):
        odd_count = 0
        for j in range(n):
            if s[i + j] != s[i + n - 1 - j]:
                odd_count += 1
        if odd_count == 1:
            odd_char = s[i:i + n][n // 2]
            if odds[odd_char] == 0:
                odds[odd_char] = 1
                palindromes.add(s[i:i + n])
    return palindromes