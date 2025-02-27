import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 193
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + n - 1 < rows and c + n - 1 < cols and (np.sum(matrix[r:r + n, c:c + n]) == 193 * 193):
                count += 1
    return count