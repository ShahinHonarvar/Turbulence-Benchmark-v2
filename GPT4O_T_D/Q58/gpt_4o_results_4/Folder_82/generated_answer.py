import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if matrix.size < 99:
        return 0
    rows, cols = matrix.shape
    valid_submatrices = 0
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    submatrix = matrix[r_start:r_end + 1, c_start:c_end + 1]
                    if submatrix.size == 99:
                        valid_submatrices += 1
    return valid_submatrices