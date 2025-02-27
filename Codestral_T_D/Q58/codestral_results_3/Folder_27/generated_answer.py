import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 77
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    if np.sum(matrix[i:k, j:l]) == n:
                        count += 1
    return count