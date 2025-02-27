import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_rows, matrix_cols = matrix.shape
    for r1 in range(0, matrix_rows):
        for r2 in range(r1 + 1, matrix_rows + 1):
            for c1 in range(0, matrix_cols):
                for c2 in range(c1 + 1, matrix_cols + 1):
                    subma = matrix[r1:r2, c1:c2]
                    if np.sum(subma) == -37:
                        result.append(subma)
    return result