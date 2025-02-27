import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 88:
                for x in range(i, rows):
                    for y in range(j, cols):
                        submatrix = matrix[i:x + 1, j:y + 1]
                        if np.count_nonzero(submatrix == 88) == 88:
                            count += 1
    return count