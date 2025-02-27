import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 88
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                if np.all(matrix[i:i + n, j:j + n] == 88):
                    count += 1
    return count