import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row1 in range(num_rows):
        for row2 in range(row1, num_rows):
            for col1 in range(num_cols):
                for col2 in range(col1, num_cols):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.sum(submatrix) == 39:
                        count += 1
    return count