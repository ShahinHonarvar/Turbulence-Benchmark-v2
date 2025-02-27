import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 99
    count = 0
    for row in range(rows):
        for col in range(cols):
            for x in range(row + 1, rows + 1):
                for y in range(col + 1, cols + 1):
                    submatrix = matrix[row:x, col:y]
                    if submatrix.size == n and np.all(submatrix >= 0) and np.all(submatrix <= 99):
                        count += 1
    return count