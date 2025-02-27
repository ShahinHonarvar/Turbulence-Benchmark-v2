import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    def is_valid_submatrix(row, col, size):
        return 0 <= row < rows - size + 1 and 0 <= col < cols - size + 1
    for size in range(1, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                if size * size == 40:
                    count += 1
    return count