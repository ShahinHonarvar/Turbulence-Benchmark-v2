import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for last_col in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if np.sum(submatrix) == -15:
                        result.append(submatrix.tolist())
    return result