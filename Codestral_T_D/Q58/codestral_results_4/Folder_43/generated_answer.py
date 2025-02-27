import numpy as np

def submatrix_with_n_numbers(matrix, n=85):
    rows, cols = matrix.shape
    submatrices = 0
    for r in range(rows):
        for c in range(cols):
            for h in range(r + 1, rows + 1):
                for w in range(c + 1, cols + 1):
                    if np.sum(matrix[r:h, c:w]) == n:
                        submatrices += 1
    return submatrices