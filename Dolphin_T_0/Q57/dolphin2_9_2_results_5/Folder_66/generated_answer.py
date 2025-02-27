import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > 99:
                continue
            for i_end in range(i, matrix.shape[0]):
                for j_end in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:i_end + 1, j:j_end + 1])
                    if submatrix_sum == 99:
                        submatrices.append(matrix[i:i_end + 1, j:j_end + 1])
    return submatrices