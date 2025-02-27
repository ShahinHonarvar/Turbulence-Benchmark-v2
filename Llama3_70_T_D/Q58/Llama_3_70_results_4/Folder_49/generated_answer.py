import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    n = 72
    size = int(np.sqrt(n))
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            submatrix = matrix[i:i + size, j:j + size]
            if submatrix.size == n:
                count += 1
    return count