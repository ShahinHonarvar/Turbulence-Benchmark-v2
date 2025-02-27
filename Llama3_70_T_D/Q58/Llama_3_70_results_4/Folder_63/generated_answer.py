import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for end_col in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:end_col + 1]
                    if submatrix.size == 57:
                        count += 1
    return count