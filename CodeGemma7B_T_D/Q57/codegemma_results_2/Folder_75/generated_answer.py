import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix) - i):
                for l in range(len(matrix[0]) - j):
                    submatrix = matrix[i:i + k + 1, j:j + l + 1]
                    if np.sum(submatrix) == 16:
                        result.append(submatrix)
    return result