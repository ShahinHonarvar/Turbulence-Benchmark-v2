import numpy as np

def submatrix_with_n_numbers(matrix, n=67):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    if np.sum(matrix[r:i + 1, c:j + 1]) == n * (i - r + 1) * (j - c + 1):
                        count += 1
    return count