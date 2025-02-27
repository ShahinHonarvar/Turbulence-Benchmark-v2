import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            for row in range(i, n_rows):
                for col in range(j, n_cols):
                    sub_matrix = matrix[i:row + 1, j:col + 1]
                    if np.sum(sub_matrix) == 77:
                        submatrices.append(sub_matrix)
    return submatrices