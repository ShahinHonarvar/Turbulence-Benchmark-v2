import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == 398:
                        submatrices.append(matrix[i:k, j:l].tolist())
    return submatrices if len(submatrices) > 0 else []