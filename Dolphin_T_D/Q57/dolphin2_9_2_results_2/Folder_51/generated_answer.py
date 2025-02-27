import numpy as np

def submatrix_with_particular_sum(m):
    rows, cols = m.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = m[i:k, j:l]
                    if np.sum(submatrix) == -46:
                        submatrices.append(submatrix)
    return submatrices