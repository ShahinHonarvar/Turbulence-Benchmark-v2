import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = (len(matrix), len(matrix[0]))
    submatrices = []
    for r1 in range(m):
        for c1 in range(n):
            for r2 in range(r1 + 1, m):
                for c2 in range(c1 + 1, n):
                    total = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if total == 100:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices