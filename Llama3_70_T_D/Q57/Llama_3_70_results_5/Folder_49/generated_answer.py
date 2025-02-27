import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for last_col in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if np.sum(submatrix) == -42:
                        result.append(submatrix)
    return result