import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 997:
                result.append([[matrix[i][j]]])
            for k in range(1, min(n - i, m - j)):
                submatrix_sum = np.sum(matrix[i:i + k, j:j + k])
                if submatrix_sum == 997:
                    result.append(matrix[i:i + k, j:j + k].tolist())
    return result