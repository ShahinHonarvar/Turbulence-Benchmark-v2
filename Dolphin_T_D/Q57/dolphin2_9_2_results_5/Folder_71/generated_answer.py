import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub_matrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if sub_matrix_sum == 69:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result