import numpy as np

def submatrix_with_n_numbers(matrix, n=185):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_size in range(r, rows):
                for c_size in range(c, cols):
                    if np.sum(matrix[r:r_size + 1, c:c_size + 1]) == n * (r_size - r + 1) * (c_size - c + 1):
                        count += 1
    return count