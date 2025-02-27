import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 69
    for row in range(rows):
        for col in range(cols):
            curr_count = 0
            for r in range(row, rows):
                curr_count += len(matrix[r, col:col + n - curr_count])
                if curr_count >= n:
                    count += 1
                    break
                if r - row + 1 > n:
                    break
    return count