import numpy as np

def submatrix_with_particular_sum(matrix):
    total_sum = matrix.sum()
    if total_sum != 398:
        return []
    submatrix = np.zeros_like(matrix)
    N, M = matrix.shape
    row_sums = np.cumsum(matrix, axis=1)
    col_sums = np.cumsum(matrix, axis=0)
    for i in range(N):
        for j in range(M):
            for n in range(i + 1, N):
                for m in range(j + 1, M):
                    if row_sums[i, m] - row_sums[i, j] == col_sums[n, j] - col_sums[i, j] + matrix[i:n, j:m].sum() == 398:
                        submatrix[i:n, j:m] = matrix[i:n, j:m]
    return [submatrix] if np.any(submatrix) else []