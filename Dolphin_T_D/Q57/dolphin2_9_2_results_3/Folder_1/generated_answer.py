import numpy as np

def submatrix_with_particular_sum(m):
    submatrices = []
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            dp = np.zeros((m.shape[0], m.shape[1]))
            for ii in range(m.shape[0]):
                for jj in range(m.shape[1]):
                    dp[ii][jj] = dp[ii - 1][jj] + dp[ii][jj - 1] - dp[ii - 1][jj - 1] + m[ii - 1][jj - 1]
            for ii in range(i, m.shape[0]):
                for jj in range(j, m.shape[1]):
                    if dp[ii][jj] - dp[ii][j - 1] - dp[i - 1][jj] + dp[i - 1][j - 1] == -25:
                        submatrices.append(m[i - 1:ii, j - 1:jj])
    return submatrices