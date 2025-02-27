import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for row_size in range(1, rows - i + 1):
                for col_size in range(1, cols - j + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if np.sum(submatrix) == -82:
                        submatrices.append(submatrix.tolist())
    return submatrices