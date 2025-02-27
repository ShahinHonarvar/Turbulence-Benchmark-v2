import numpy as np

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    submatrices = []
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == -57:
                        submatrices.append(sub_matrix.tolist())
    return submatrices