import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 63
    target_sum = n * (n + 1) // 2
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows - row, cols - col) + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if len(submatrix.flatten()) == n and np.sum(submatrix) == target_sum:
                    count += 1
    return count