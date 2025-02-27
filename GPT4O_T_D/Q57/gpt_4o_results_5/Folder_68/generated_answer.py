import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, r1, c1, r2, c2):
        return np.sum(mat[r1:r2 + 1, c1:c2 + 1])
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if submatrix_sum(matrix, i, j, k, l) == 3:
                        submatrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return submatrices