import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix), i, -1):
                for l in range(len(matrix[0]), j, -1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == 41:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices