from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = len(s)
    if n < 16:
        return palindromes
    max_len = n // 2 + 1
    dp = defaultdict(int)
    for i in range(max_len):
        for j in range(n - i - 1):
            dp[i, j] = dp[i, j + 1] or (s[j] == s[n - i - j - 1] and (i <= 1 or dp[i - 2, j]))
            if dp[i, j] and i + 1 >= 16:
                palindromes.add(s[j:j + i + 1])
    return palindromes