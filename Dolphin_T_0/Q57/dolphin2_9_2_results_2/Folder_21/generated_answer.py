import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == -936:
                        result.append(matrix[i:k, j:l])
    return result