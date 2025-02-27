import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n - 1):
        for j in range(m - 1):
            for x in range(i + 1, n):
                for y in range(j + 1, m):
                    sub_matrix = matrix[i:x, j:y]
                    if np.sum(sub_matrix) == 394:
                        submatrices.append(sub_matrix)
    return submatrices