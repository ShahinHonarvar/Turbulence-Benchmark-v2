import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for x in range(i, r):
                for y in range(j, c):
                    sub = np.array(matrix[i:x + 1, j:y + 1])
                    if np.sum(sub) == 394:
                        submatrices.append(sub.tolist())
    return submatrices