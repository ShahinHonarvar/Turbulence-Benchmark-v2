import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if len(sub_matrix) * len(sub_matrix[0]) == 83:
                        count += 1
    return count