import numpy as np

def submatrix_with_particular_sum(matrix):
    nrow, ncol = matrix.shape
    submatrices = []
    for i in range(nrow):
        for j in range(ncol):
            for x in range(i, nrow):
                for y in range(j, ncol):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == -936:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices