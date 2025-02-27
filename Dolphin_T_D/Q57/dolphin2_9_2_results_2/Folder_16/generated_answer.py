import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for subsize in range(1, min(matrix.shape)):
        for row_start in range(matrix.shape[0] - subsize + 1):
            for col_start in range(matrix.shape[1] - subsize + 1):
                submatrix = matrix[row_start:row_start + subsize, col_start:col_start + subsize]
                if np.sum(submatrix) == -157:
                    submatrices.append(submatrix)
    return submatrices