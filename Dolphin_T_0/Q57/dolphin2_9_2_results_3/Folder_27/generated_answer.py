import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i, matrix.shape[0]):
                for n in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:m + 1, j:n + 1])
                    if submatrix_sum == 77:
                        result.append(matrix[i:m + 1, j:n + 1])
    return result