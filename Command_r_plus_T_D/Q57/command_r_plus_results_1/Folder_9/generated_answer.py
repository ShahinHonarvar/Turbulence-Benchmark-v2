import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def submatrix_sums(matrix):
        n = matrix.shape[0]
        m = matrix.shape[1]
        submatrix_sums = np.zeros((n, m))
        submatrix_sums[0, :] = np.cumsum(matrix[0, :])
        submatrix_sums[:, 0] = np.cumsum(matrix[:, 0])
        for i in range(1, n):
            for j in range(1, m):
                submatrix_sums[i, j] = submatrix_sums[i - 1, j] + submatrix_sums[i, j - 1] - submatrix_sums[i - 1, j - 1] + matrix[i, j]
        return submatrix_sums

    def find_submatrices(sums, target_sum):
        n, m = sums.shape
        submatrices = []
        for i in range(n):
            for j in range(m):
                for size_i in range(n - i + 1):
                    for size_j in range(m - j + 1):
                        if i + size_i <= n and j + size_j <= m:
                            if sums[i + size_i - 1, j + size_j - 1] - (sums[i - 1, j + size_j - 1] if i > 0 else 0) - (sums[i + size_i - 1, j - 1] if j > 0 else 0) + (sums[i - 1, j - 1] if i > 0 and j > 0 else 0) == target_sum:
                                submatrices.append(matrix[i:i + size_i, j:j + size_j])
        return submatrices
    sums = submatrix_sums(matrix)
    target_sum = -86
    return find_submatrices(sums, target_sum)