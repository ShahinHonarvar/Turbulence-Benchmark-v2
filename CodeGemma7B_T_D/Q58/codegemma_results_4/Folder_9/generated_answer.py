import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            for r1 in range(r, matrix.shape[0]):
                for c1 in range(c, matrix.shape[1]):
                    submatrix = matrix[r:r1 + 1, c:c1 + 1]
                    if np.count_nonzero(submatrix == 33) == 33:
                        count += 1
    return count