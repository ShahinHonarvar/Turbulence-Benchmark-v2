import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 92
    submatrix_size = int(np.sqrt(n))
    for row in range(rows - submatrix_size + 1):
        for col in range(cols - submatrix_size + 1):
            submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
            if submatrix.size == n:
                count += 1
    return count