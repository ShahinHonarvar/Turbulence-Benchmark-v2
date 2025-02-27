import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 68
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - int(np.sqrt(n)) + 1):
        for col in range(cols - int(np.sqrt(n)) + 1):
            for size in range(int(np.sqrt(n)), min(rows - row, cols - col) + 1):
                if size * size == n:
                    count += 1
    return count