import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    for i in range(matrix_height):
        for j in range(matrix_width):
            if matrix[i][j] == 1:
                for k in range(matrix_height):
                    for l in range(matrix_width):
                        if k > i + 1 or l > j + 1 or k < i or (l < j):
                            continue
                        if np.prod(matrix[k - i][l - j]) == 118:
                            count += 1
    return count