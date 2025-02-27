import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            for k in range(i + 1, rows):
                for last_col in range(j + 1, cols):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if submatrix.size == 16:
                        count += 1
    return count