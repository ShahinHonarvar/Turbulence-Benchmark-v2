import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix) + 1):
                    current_submatrix = matrix[i:k, j:l]
                    if np.sum(current_submatrix) == -81:
                        result.append(current_submatrix)
    return result