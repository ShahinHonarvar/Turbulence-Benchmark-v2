def find_subset_of_length_n(s):
    if len(s) < 97:
        return 0
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j] + (1 << j) * dp[i - 1][j - 1]
    result = 0
    for i in range(1, n + 1):
        result += (1 << i) * dp[n][i]
    return result