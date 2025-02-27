import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for row_length in range(1, rows - i + 1):
                for col_length in range(1, cols - j + 1):
                    submatrix_sum = np.sum(matrix[i:i + row_length, j:j + col_length])
                    if submatrix_sum == 13:
                        submatrices.append(matrix[i:i + row_length, j:j + col_length])
    return submatrices