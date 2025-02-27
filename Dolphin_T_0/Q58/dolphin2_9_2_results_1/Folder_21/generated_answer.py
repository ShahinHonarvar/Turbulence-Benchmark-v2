import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_len = len(matrix)
    submatrix_count = 0
    for i in range(matrix_len):
        for j in range(matrix_len):
            if matrix[i][j] == 139:
                for k in range(i, matrix_len):
                    if k == i:
                        if sum(matrix[k][j:j + 140]) == 139 * 140:
                            submatrix_count += 1
                    elif sum(matrix[k][j:j + 140]) + sum(matrix[i:k + 1][j]) - matrix[k][j] == 139 * 140:
                        submatrix_count += 1
    return submatrix_count