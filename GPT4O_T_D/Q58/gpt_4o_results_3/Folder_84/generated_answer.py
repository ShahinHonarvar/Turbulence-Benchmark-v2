import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    submatrix_size = 127
    for r_start in range(rows):
        for r_end in range(r_start + 1, rows + 1):
            for c_start in range(cols):
                for c_end in range(c_start + 1, cols + 1):
                    if (r_end - r_start) * (c_end - c_start) == submatrix_size:
                        submatrix = matrix[r_start:r_end, c_start:c_end]
                        if submatrix.size == submatrix_size:
                            count += 1
    return count