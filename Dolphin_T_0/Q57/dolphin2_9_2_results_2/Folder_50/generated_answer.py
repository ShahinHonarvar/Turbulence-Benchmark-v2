import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 95:
                        results.append(submatrix)
    return results