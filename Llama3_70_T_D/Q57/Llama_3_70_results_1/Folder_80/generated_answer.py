import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for last_col in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:last_col + 1])
                    if submatrix_sum == 245:
                        result.append(matrix[i:k + 1, j:last_col + 1].tolist())
    return result