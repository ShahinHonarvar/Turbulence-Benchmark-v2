import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rlen, clen = matrix.shape
    for i1 in range(rlen):
        for i2 in range(i1, rlen):
            for j1 in range(clen):
                for j2 in range(j1, clen):
                    submatrix_sum = np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
                    if submatrix_sum == -86:
                        submatrices.append(matrix[i1:i2 + 1, j1:j2 + 1])
    return submatrices