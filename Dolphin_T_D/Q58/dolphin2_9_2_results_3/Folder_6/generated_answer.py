import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1:
                if i + 10 < num_rows and j + 10 < num_cols:
                    submatrix = matrix[i:i + 11, j:j + 11]
                    if np.sum(submatrix) == 122:
                        submatrix_count += 1
    return submatrix_count