import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    dimx = len(matrix[0])
    dimy = len(matrix)
    for i in range(dimx):
        for j in range(dimy):
            for k in range(i, dimx):
                for l in range(j, dimy):
                    submatrix = matrix[l - j:l - j + i - k + 1, k - i:k - i + dimy - l + j - 1]
                    if np.sum(submatrix) == 28:
                        submatrices.append(submatrix)
    if not submatrices:
        return []
    return submatrices