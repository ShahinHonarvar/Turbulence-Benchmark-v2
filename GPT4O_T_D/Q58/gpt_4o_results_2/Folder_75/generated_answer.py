import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 80
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    total_elements = matrix.size
    if total_elements < submatrix_size:
        return 0
    rows, cols = matrix.shape
    submatrix_count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            elements_counted = 0
            for row in range(start_row, rows):
                for col in range(start_col, cols):
                    elements_counted += 1
                    if elements_counted == submatrix_size:
                        submatrix_count += 1
                        break
                if elements_counted >= submatrix_size:
                    break
    return submatrix_count