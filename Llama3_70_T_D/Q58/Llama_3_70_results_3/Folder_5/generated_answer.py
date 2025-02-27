import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = int(np.sqrt(63))
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == 63:
                count += 1
    return count