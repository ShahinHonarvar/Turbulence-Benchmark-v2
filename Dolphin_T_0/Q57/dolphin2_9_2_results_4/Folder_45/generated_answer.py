import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i_start in range(matrix.shape[0]):
        for i_end in range(i_start + 1, matrix.shape[0] + 1):
            for j_start in range(matrix.shape[1]):
                for j_end in range(j_start + 1, matrix.shape[1] + 1):
                    submatrix_sum = np.sum(matrix[i_start:i_end, j_start:j_end])
                    if submatrix_sum == -77:
                        submatrices.append(matrix[i_start:i_end, j_start:j_end])
    return submatrices