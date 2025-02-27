import numpy as np

def submatrix_with_particular_sum(matrix):
    row_indices = range(0, matrix.shape[0])
    col_indices = range(0, matrix.shape[1])
    submatrices = []
    for i in row_indices:
        for j in col_indices:
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    submatrix_sum = np.sum(matrix[i:x, j:y])
                    if submatrix_sum == -61:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices