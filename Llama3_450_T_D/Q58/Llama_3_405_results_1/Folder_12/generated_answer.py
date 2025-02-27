import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 46
    for row in range(rows):
        for col in range(cols):
            for row_size in range(1, rows - row + 1):
                for col_size in range(1, cols - col + 1):
                    if row_size * col_size == n:
                        submatrix = matrix[row:row + row_size, col:col + col_size]
                        if np.size(submatrix) == n:
                            count += 1
    return count