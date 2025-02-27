import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for end_col in range(j + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:k, j:end_col]
                    if np.sum(submatrix) == -936:
                        result.append(submatrix)
    return result