import numpy as np

def submatrix_with_particular_sum(matrix):
    i_max, j_max = matrix.shape
    i_min, j_min = (0, 0)
    submatrix_result = []
    for i in range(i_max):
        for j in range(j_max):
            for i_min in range(i, i_max):
                for j_min in range(j, j_max):
                    submatrix = matrix[i:i_min + 1, j:j_min + 1]
                    if np.sum(submatrix) == -4:
                        submatrix_result.append(submatrix)
    return submatrix_result