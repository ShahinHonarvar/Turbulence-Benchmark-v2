import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 66
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submat = matrix[i:i + n, j:j + n]
                if np.count_nonzero(submat) == n:
                    count += 1
    return count