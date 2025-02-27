import numpy as np

def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if np.sum(submatrix) == -936:
                        return submatrix
    return []