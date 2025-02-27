import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for x in range(i + 1, r + 1):
                for y in range(j + 1, c + 1):
                    submatrix = matrix[i:x, j:y]
                    if np.sum(submatrix) == 901:
                        submatrices.append(submatrix)
    return submatrices