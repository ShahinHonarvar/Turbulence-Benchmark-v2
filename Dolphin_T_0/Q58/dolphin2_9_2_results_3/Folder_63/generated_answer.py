import numpy as np

def submatrix_with_n_numbers(matrix, n=57):
    submatrices = 0
    sub_matrix_length = len(matrix[0])
    sub_matrix_width = len(matrix)
    for i in range(sub_matrix_width):
        for j in range(sub_matrix_length):
            if matrix[i][j] == n:
                for x in range(i + 1, sub_matrix_width):
                    if np.all(matrix[x][j:j + 1] == n):
                        if len(matrix[x][j:j + 1]) == n:
                            submatrices += 1
                        else:
                            break
                    else:
                        break
    return submatrices