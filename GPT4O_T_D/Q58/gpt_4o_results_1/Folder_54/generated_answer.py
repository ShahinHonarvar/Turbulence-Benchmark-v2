import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            for sub_r in range(r + 1, num_rows + 1):
                for sub_c in range(c + 1, num_cols + 1):
                    submatrix = matrix[r:sub_r, c:sub_c]
                    if submatrix.size == 27:
                        count += 1
    return count