import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for r in range(row, matrix.shape[0]):
                for c in range(col, matrix.shape[1]):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.count_nonzero(submatrix == 95) == 95:
                        count += 1
    return count