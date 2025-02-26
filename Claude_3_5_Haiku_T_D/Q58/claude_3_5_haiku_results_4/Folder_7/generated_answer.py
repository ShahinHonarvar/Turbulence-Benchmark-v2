import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for height in range(1, rows + 1):
        for width in range(1, cols + 1):
            for r_start in range(rows - height + 1):
                for c_start in range(cols - width + 1):
                    submatrix = matrix[r_start:r_start + height, c_start:c_start + width]
                    if submatrix.size == 121:
                        count += 1
    return count