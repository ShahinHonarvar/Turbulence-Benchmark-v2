import numpy as np

def submatrix_with_n_numbers(matrix, n=120):
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if (r - i + 1) * (c - j + 1) == n and np.sum(matrix[i:r + 1, j:c + 1]) == n:
                        counter += 1
    return counter