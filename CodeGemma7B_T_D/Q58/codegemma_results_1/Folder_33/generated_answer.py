import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = np.shape(matrix)
    count = 0
    for r in range(rows):
        for c in range(cols):
            for row in range(r, rows):
                for col in range(c, cols):
                    submatrix = matrix[r:row + 1, c:col + 1]
                    if np.count_nonzero(submatrix == 118) == 118:
                        count += 1
    return count