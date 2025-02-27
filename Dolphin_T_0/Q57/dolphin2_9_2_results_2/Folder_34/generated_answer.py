import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    current_submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(current_submatrix) == -13:
                        result.append(current_submatrix.tolist())
    return result