import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for h in range(r, rows):
                for w in range(c, cols):
                    submatrix = matrix[r:h + 1, c:w + 1]
                    if submatrix.size == 176 and np.all(submatrix == 176):
                        count += 1
    return count