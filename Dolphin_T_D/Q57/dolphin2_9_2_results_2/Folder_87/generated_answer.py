import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for a in range(i + 1, len(matrix) + 1):
                for b in range(j + 1, len(matrix[0]) + 1):
                    submatrix = np.array(matrix[i:a, j:b])
                    if np.sum(submatrix) == 35:
                        result.append(submatrix)
    return result