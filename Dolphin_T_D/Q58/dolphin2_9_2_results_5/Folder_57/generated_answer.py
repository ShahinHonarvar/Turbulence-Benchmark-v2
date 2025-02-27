import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 92:
                        submatrix_count += 1
    return submatrix_count