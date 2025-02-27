import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 121
    rows, cols = matrix.shape
    for row in range(rows - int(np.sqrt(n)) + 1):
        for col in range(cols - int(np.sqrt(n)) + 1):
            submatrix = matrix[row:row + int(np.sqrt(n)), col:col + int(np.sqrt(n))]
            if submatrix.size == n:
                count += 1
    return count