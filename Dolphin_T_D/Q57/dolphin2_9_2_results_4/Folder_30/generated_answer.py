import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    temp = np.sum(matrix[i:k + 1, j:l + 1])
                    if temp == 21:
                        result.append(matrix[i:k + 1, j:l + 1].tolist())
    return result