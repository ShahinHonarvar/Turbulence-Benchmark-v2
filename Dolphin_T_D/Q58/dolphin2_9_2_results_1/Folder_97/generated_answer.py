import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 120
    matrix_size = len(matrix) * len(matrix[0])
    if matrix_size < target_size:
        return 0
    count_submatrices = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(max(0, i + 1 - target_size), i + 1):
                for l in range(max(0, j + 1 - target_size), j + 1):
                    if len(np.unique(matrix[k:i + 1, l:j + 1])) * (i + 1 - k) * (j + 1 - l) == target_size:
                        count_submatrices += 1
    return count_submatrices