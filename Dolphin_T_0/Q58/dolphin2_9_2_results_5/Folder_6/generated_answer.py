import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 122:
                for k in range(i, m):
                    for l in range(j, n):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.count_nonzero(submatrix == 122) == 122:
                            count += 1
    return count