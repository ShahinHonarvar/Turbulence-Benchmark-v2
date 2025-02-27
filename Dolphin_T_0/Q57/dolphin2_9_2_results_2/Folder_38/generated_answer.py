import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    m, n = matrix.shape
    for x in range(m):
        for y in range(n):
            for z in range(x + 1, m):
                for a in range(y + 1, n):
                    if np.sum(matrix[x:z, y:a]) == 34:
                        sub_matrices.append(matrix[x:z, y:a])
    return sub_matrices