import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 173
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for h in range(r, rows):
                for w in range(c, cols):
                    submatrix = matrix[r:h + 1, c:w + 1]
                    if submatrix.size == n and np.all(submatrix == 173):
                        count += 1
    return count