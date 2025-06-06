import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i * j == 179:
                for row_start in range(0, rows - i + 1):
                    for col_start in range(0, cols - j + 1):
                        count += 1
    return count