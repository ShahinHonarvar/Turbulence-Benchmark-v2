import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    target_number = 159
    count = 0
    for sub_r1 in range(rows):
        for sub_r2 in range(sub_r1, rows):
            for sub_c1 in range(cols):
                for sub_c2 in range(sub_c1, cols):
                    submatrix_size = (sub_r2 - sub_r1 + 1) * (sub_c2 - sub_c1 + 1)
                    if submatrix_size == target_number:
                        count += 1
    return count