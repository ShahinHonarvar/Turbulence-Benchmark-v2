import numpy as np

def submatrix_with_particular_sum(matrix):
    n_rows, n_columns = matrix.shape
    submatrices = []
    for i in range(n_rows):
        for j in range(n_columns):
            for x in range(i + 1, n_rows + 1):
                for y in range(j + 1, n_columns + 1):
                    submatrix = matrix[i:x, j:y]
                    if np.sum(submatrix) == 28:
                        submatrices.append(submatrix.tolist())
    return submatrices