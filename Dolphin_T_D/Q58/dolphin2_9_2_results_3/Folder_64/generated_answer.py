import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    if len(np.array([matrix[i][j], matrix[i][l], matrix[k][j], matrix[k][l], matrix[i][(j + l) // 2], matrix[(i + k) // 2][j], matrix[(i + k) // 2][l]])) == 7:
                        count += 1
    return count