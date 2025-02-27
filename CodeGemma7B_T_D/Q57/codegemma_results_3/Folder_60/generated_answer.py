import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_of_matrix = np.sum(matrix)
    if sum_of_matrix != 94:
        return []
    result = []
    for i in range(matrix.shape[0] + 1):
        for j in range(matrix.shape[1] + 1):
            for k in range(i):
                for l in range(j):
                    submatrix = matrix[k:i, l:j]
                    if np.sum(submatrix) == 94:
                        result.append(submatrix)
    return result