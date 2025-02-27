import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    if n == 0:
        return []
    m = len(matrix[0])
    if m == 0:
        return []
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
    submatrices = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i - 1, -1, -1):
                for l in range(j - 1, -1, -1):
                    if dp[i][j] - dp[i][l] - dp[k][j] + dp[k][l] == -617:
                        submatrices.append(matrix[k:i, l:j])
    return submatrices