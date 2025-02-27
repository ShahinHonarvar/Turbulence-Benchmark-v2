import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    sm = np.sum(matrix[i:k, j:l])
                    if sm == 69:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices if submatrices else []