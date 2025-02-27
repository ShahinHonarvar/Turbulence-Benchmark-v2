import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n - 5):
        for j in range(m - 5):
            if np.sum(matrix[i:i + 6, j:j + 6]) == 91:
                count += 1
    return count