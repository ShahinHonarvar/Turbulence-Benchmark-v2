import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0] * matrix.shape[1]
    submatrix_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 13:
                for k in range(i, matrix.shape[0]):
                    for l in range(j, matrix.shape[1]):
                        sub_matrix = matrix[i:k + 1, j:l + 1]
                        submatrix_elements = len(sub_matrix.flatten())
                        if sub_matrix.count(13) == 1 and submatrix_elements == 13:
                            submatrix_count += 1
    return submatrix_count