import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for r in range(i, matrix.shape[0]):
                for c in range(j, matrix.shape[1]):
                    submatrix = matrix[i:r + 1, j:c + 1]
                    if np.sum(submatrix) == 43:
                        submatrix_count += 1
    return submatrix_count