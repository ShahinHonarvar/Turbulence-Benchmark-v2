import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 88:
                submatrix = matrix[i - 1:i + 2, j - 1:j + 2]
                if np.all(submatrix == 88):
                    count += 1
    return count