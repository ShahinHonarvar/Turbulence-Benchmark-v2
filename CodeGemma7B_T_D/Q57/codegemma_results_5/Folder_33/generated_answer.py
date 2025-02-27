import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sum_of_submatrix = np.sum(matrix[i:k + 1, j:l + 1])
                    if sum_of_submatrix == -811:
                        results.append(matrix[i:k + 1, j:l + 1])
    return results