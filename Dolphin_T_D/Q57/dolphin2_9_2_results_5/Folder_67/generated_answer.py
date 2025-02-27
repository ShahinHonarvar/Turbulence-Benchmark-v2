import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = len(matrix)
    for x in range(n):
        for y in range(n):
            for size in range(2, n - max(x, y) + 1):
                sub = matrix[x:x + size, y:y + size]
                if np.sum(sub) == 40:
                    submatrices.append(sub)
    return submatrices