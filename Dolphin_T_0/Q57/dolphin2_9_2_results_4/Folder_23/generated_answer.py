import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if k - i + 1 == 1 and l - j + 1 == 1:
                        if matrix[i, j] == 59:
                            submatrices.append(matrix[i:k + 1, j:l + 1])
                    elif k - i + 1 == 2 and l - j + 1 == 2:
                        if matrix[i, j] + matrix[i, j + 1] + matrix[i + 1, j] + matrix[i + 1, j + 1] == 59:
                            submatrices.append(matrix[i:k + 1, j:l + 1])
                    elif l - j + 1 == 1:
                        if np.sum(matrix[i:k + 1, j]) == 59:
                            submatrices.append(matrix[i:k + 1, j])
                    elif k - i + 1 == 1:
                        if np.sum(matrix[i, j:l + 1]) == 59:
                            submatrices.append(matrix[i, j:l + 1])
                    elif np.sum(matrix[i:k + 1, j:l + 1]) == 59:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices