import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, n + 1):
                    sub_matrix_sum = np.sum(matrix[i:k, j:l])
                    if sub_matrix_sum == -3:
                        submatrices.append(matrix[i:k, j:l])
                    else:
                        continue
    if not submatrices:
        return []
    else:
        return submatrices