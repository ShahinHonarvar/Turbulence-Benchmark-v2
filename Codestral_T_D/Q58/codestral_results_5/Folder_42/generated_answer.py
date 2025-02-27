import numpy as np

def submatrix_with_n_numbers(matrix, n=193):
    rows, cols = matrix.shape
    total = 0
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    submatrix = matrix[r:i + 1, c:j + 1]
                    if np.size(submatrix) == n and np.all(submatrix == 193):
                        total += 1
    return total