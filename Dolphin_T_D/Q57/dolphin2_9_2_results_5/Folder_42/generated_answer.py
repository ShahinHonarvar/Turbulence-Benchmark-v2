import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    sub = np.array(matrix[r1:r2 + 1, c1:c2 + 1])
                    if np.sum(sub) == 862:
                        submatrices.append(sub.tolist())
    return submatrices