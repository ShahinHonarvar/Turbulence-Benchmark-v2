def find_subset_of_length_n(s):
    if len(s) < 616:
        return 0
    else:
        n = len(s)
        subset_size = 616
        dp = [[0 for _ in range(subset_size + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, subset_size + 1):
                if s[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - s[i - 1]]
        return dp[n][subset_size]