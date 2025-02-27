import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix) - i):
                for l in range(len(matrix[0]) - j):
                    sub = np.sum(matrix[i:i + k, j:j + l])
                    if sub == 40:
                        result.append(matrix[i:i + k, j:j + l])
    return result