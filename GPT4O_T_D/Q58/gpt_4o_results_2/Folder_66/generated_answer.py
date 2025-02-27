import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    target_count = 42
    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for row in range(n - i + 1):
                for col in range(m - j + 1):
                    submatrix = matrix[row:row + i, col:col + j]
                    if submatrix.size == target_count:
                        count += 1
    return count