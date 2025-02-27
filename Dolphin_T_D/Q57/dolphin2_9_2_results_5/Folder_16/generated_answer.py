import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -157:
                        result.append(submatrix)
    return result