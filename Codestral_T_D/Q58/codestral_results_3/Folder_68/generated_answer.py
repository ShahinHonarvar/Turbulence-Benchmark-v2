import numpy as np

def submatrix_with_n_numbers(matrix, n=74):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for h in range(r, rows):
                for w in range(c, cols):
                    if np.size(matrix[r:h + 1, c:w + 1]) == n:
                        count += 1
    return count