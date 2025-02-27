import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    sub = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub) == 77:
                        submatrices.append(sub.tolist())
    return submatrices