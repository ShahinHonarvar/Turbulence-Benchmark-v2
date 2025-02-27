import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    numbers = np.prod(matrix.shape)
    if numbers % 146 != 0:
        return 0
    n_submatrices = numbers // 146
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                for k in range(i, rows):
                    for l in range(j, cols):
                        if k - i + 1 == n_submatrices and l - j + 1 == n_submatrices:
                            if (k - i + 1) * (l - j + 1) == 146:
                                submatrix_count += 1
    return submatrix_count