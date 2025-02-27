def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    palindromes = set()
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    if j - i + 1 >= 30:
                        palindromes.add(s[i:j + 1])
    return palindromes