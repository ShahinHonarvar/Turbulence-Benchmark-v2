import numpy as np

def submatrix_with_n_numbers(matrix):
    a, b = matrix.shape
    count = 0
    for i in range(a):
        for j in range(b):
            if a - i >= 4 and b - j >= 4:
                if np.count_nonzero(matrix[i:i + 4, j:j + 4]) == 66:
                    count += 1
    return count