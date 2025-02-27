import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix[0]) * len(matrix[1])
    if n == 138:
        for i in range(len(matrix[0]) - 2):
            for j in range(len(matrix[1]) - 1):
                if np.count_nonzero(matrix[i:i + 2, j:j + 3]) == 138:
                    return 1
    return 0