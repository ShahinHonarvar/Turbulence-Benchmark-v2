import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_rows, matrix_cols = matrix.shape
    for h in range(matrix_rows):
        for w in range(matrix_cols):
            for z in range(h, matrix_rows):
                for c in range(w, matrix_cols):
                    if np.sum(matrix[h:z + 1, w:c + 1]) == -157:
                        submatrices.append(matrix[h:z + 1, w:c + 1])
    return submatrices