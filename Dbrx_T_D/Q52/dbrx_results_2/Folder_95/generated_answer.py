from collections import defaultdict

def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 87:
        return set()
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(s)):
            dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
    palindromes = set()
    for i in range(len(s) - 87 + 1):
        for j in range(i, i + 87):
            if dp[i][j]:
                palindrome = s[i:j + 1]
                palindromes.add(palindrome)
    return palindromes