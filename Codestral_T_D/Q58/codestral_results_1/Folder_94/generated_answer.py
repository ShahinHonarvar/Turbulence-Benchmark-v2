import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 93:
                submatrix_size = 1
                while i + submatrix_size <= rows and j + submatrix_size <= cols:
                    submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                    if submatrix.size == 93 and np.all(submatrix == 93):
                        count += 1
                    submatrix_size += 1
    return count