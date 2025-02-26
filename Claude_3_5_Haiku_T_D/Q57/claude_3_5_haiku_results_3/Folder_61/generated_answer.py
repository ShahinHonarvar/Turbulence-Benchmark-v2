import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for row_start in range(m):
        for row_end in range(row_start, m):
            for col_start in range(n):
                for col_end in range(col_start, n):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == 8:
                        result.append(submatrix.tolist())
    return result