import numpy as np

def submatrix_with_n_numbers(matrix):
    sum_matrix = matrix + 0
    sum_matrix = np.cumsum(sum_matrix, axis=0)
    sum_matrix = np.cumsum(sum_matrix, axis=1)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for length in range(i + 1):
                for step in range(j + 1):
                    submatrix_sum = sum_matrix[i, j] - sum_matrix[i - length, j] - sum_matrix[i, j - step] + sum_matrix[i - length, j - step]
                    if submatrix_sum == 144:
                        return submatrix_sum
    return 0