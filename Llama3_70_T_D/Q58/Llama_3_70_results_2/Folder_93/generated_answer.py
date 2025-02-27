import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 53
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for h in range(row, rows):
                for w in range(col, cols):
                    submatrix = matrix[row:h + 1, col:w + 1]
                    if np.prod(submatrix.shape) == n:
                        count += 1
    return count