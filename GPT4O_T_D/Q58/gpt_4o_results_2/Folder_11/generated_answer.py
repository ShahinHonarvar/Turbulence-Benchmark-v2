import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    min_elements = 38
    count = 0
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    if (r_end - r_start + 1) * (c_end - c_start + 1) == min_elements:
                        count += 1
    return count