import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_sum = np.sum(matrix)
    target_sum = -863
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == target_sum:
                        result.append(matrix[i:k + 1, j:l + 1])
    if np.sum(result) != matrix_sum:
        return []
    return result