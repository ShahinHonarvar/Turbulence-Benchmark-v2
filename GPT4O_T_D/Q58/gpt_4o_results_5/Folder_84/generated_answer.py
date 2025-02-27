import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 127:
        return 0
    total_submatrices = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 127:
                for start_row in range(rows - r + 1):
                    for start_col in range(cols - c + 1):
                        total_submatrices += 1
    return total_submatrices