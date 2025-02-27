from collections import defaultdict

def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 188:
        return set()
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if s[i] == s[j] and k == 1:
                dp[i][j] = True
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
    palindromes = set()
    for i in range(n - 188 + 1):
        for j in range(i, i + 188):
            if dp[i][j]:
                palindromes.add(s[i:j + 1])
    return palindromes