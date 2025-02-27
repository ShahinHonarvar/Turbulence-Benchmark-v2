import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    rows_limit = rows * cols < 186
    cols_limit = 186 // rows + (0 if 186 % rows == 0 else 1) > cols
    if rows_limit or cols_limit:
        return 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 186:
                for i in range(rows - r + 1):
                    for j in range(cols - c + 1):
                        count += 1
    return count