import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    row_sums = np.zeros((m + 1, n + 1), dtype=int)
    submatrices = []
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            row_sums[i, j] = row_sums[i - 1, j] + row_sums[i, j - 1] - row_sums[i - 1, j - 1] + matrix[i - 1, j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, min(i, j) + 1):
                _sum = row_sums[i, j] - row_sums[i - k, j] - row_sums[i, j - k] + row_sums[i - k, j - k]
                if _sum == -37:
                    submatrices.append(matrix[i - k:i, j - k:j])
    return submatrices