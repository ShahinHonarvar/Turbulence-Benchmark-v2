import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 131
    for row in range(rows):
        for col in range(cols):
            for r in range(row + 1, rows + 1):
                for c in range(col + 1, cols + 1):
                    submatrix = matrix[row:r, col:c]
                    if np.count_nonzero(submatrix) == n:
                        count += 1
    return count