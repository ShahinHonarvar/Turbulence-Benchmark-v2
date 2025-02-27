import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for i_end in range(i, matrix.shape[0]):
                for j_end in range(j, matrix.shape[1]):
                    sub_matrix_sum = np.sum(matrix[i:i_end + 1, j:j_end + 1])
                    if sub_matrix_sum == -13:
                        result.append(matrix[i:i_end + 1, j:j_end + 1])
    return result