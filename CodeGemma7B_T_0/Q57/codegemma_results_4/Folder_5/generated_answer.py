import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -43:
                        submatrices.append(submatrix)
    return submatrices