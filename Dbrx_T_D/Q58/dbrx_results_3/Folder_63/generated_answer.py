import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i, min(i + 57, n_rows)):
                for l in range(j, min(j + 57, n_cols)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.all(submatrix == 57):
                        count += 1
    return count