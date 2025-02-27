def find_subset_of_length_n(s):
    if len(s) < 89:
        return 0
    n = len(s)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * (n - i + 1) / i
    return int(dp[89])