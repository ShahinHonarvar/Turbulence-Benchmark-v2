import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    for row in range(mat.shape[0]):
        for col in range(mat.shape[1]):
            for row2 in range(row, mat.shape[0]):
                for col2 in range(col, mat.shape[1]):
                    submatrix = mat[row:row2 + 1, col:col2 + 1]
                    if np.sum(submatrix) == 144:
                        count += 1
    return count