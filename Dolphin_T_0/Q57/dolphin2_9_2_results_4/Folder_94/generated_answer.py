import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    s = 92
    n = len(matrix)
    for x in range(n):
        for y in range(n):
            for i in range(x, n):
                for j in range(y, n):
                    submatrix = np.array(matrix[x:i + 1, y:j + 1])
                    if np.sum(submatrix) == s:
                        result.append(submatrix)
    return result