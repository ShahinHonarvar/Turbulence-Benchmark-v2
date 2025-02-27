from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    n = 113
    if len(s) < n:
        return set()
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[-1][i] = dp[i][-1] = True
    for k in range(2, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and (k < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
    palindromes = set()
    for i in range(n):
        for j in range(i, i + n):
            if dp[i][j]:
                palindromes.add(s[i:j + 1])
    return palindromes