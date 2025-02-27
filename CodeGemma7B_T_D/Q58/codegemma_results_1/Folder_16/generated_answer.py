import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row1 in range(num_rows):
        for row2 in range(row1 + 1, num_rows + 1):
            for col1 in range(num_cols):
                for col2 in range(col1 + 1, num_cols + 1):
                    submatrix = matrix[row1:row2, col1:col2]
                    if np.sum(submatrix) == 154:
                        count += 1
    return count