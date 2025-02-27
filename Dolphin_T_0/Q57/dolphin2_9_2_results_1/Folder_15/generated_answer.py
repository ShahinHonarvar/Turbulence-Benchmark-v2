import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    N = len(matrix)
    for x in range(N):
        for y in range(N):
            for size in range(1, min(N - x, N - y) + 1):
                submatrix_sum = np.sum(matrix[x:x + size, y:y + size])
                if submatrix_sum == -9:
                    submatrices.append(matrix[x:x + size, y:y + size])
    return submatrices if len(submatrices) > 0 else []