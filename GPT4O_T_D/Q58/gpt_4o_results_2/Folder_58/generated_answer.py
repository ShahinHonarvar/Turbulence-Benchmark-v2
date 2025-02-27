import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    row_count, col_count = matrix.shape
    count = 0
    for r in range(1, row_count + 1):
        for c in range(1, col_count + 1):
            if r * c == 185:
                for i in range(row_count - r + 1):
                    for j in range(col_count - c + 1):
                        count += 1
    return count