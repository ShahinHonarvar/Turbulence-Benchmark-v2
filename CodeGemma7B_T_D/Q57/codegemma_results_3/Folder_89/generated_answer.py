import numpy as np

def submatrix_with_particular_sum(mat):

    def generate_submatrix(i1, j1, i2, j2):
        submatrix = np.zeros((i2 - i1 + 1, j2 - j1 + 1))
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                submatrix[i - i1][j - j1] = mat[i][j]
        return submatrix
    rows, cols = mat.shape
    submatrices = []
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    submatrix = generate_submatrix(i1, j1, i2, j2)
                    if np.sum(submatrix) == 80:
                        submatrices.append(submatrix)
    return submatrices