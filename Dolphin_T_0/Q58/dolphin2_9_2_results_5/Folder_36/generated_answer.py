import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 131
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - n + 1):
        for c in range(cols - n + 1):
            if (matrix[r:r + n, c:c + n].sum() == n * n * n).all():
                count += 1
    return count