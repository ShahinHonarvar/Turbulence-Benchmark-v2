from collections import defaultdict

def palindrome_of_length_n(s: str) -> set:
    n = 318
    s = s.lower()
    palindromes = set()
    length = len(s)
    if length < n:
        return palindromes
    dp = [[False] * n for _ in range(length)]
    for i in range(length):
        dp[i][0] = True
        if i >= 1 and s[i - 1] == s[i]:
            dp[i][1] = True
    for k in range(2, n):
        for i in range(length - k + 1):
            dp[i][k] = dp[i][k - 2] and s[i] == s[i + k - 1]
    for i in range(length - n + 1):
        if dp[i][n]:
            palindromes.add(s[i:i + n])
    return palindromes