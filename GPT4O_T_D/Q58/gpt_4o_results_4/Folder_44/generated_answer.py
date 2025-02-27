import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    m, n = matrix.shape
    count = 0
    submatrix_size = 191
    submatrix_count = int(np.ceil(submatrix_size ** 0.5))
    if submatrix_count > m or submatrix_count > n:
        return 0
    for i in range(m - submatrix_count + 1):
        for j in range(n - submatrix_count + 1):
            for sub_i in range(submatrix_count, min(m - i + 1, n - j + 1) + 1):
                if sub_i * sub_i == submatrix_size:
                    count += (m - i - sub_i + 1) * (n - j - sub_i + 1)
    return count