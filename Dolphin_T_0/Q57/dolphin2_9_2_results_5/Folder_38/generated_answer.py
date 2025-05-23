import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 34:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices