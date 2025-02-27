import numpy as np

def submatrix_with_n_numbers(matrix, n=57):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    if (i - r + 1) * (j - c + 1) == n:
                        if np.all(matrix[r:i + 1, c:j + 1] == 57):
                            count += 1
    return count