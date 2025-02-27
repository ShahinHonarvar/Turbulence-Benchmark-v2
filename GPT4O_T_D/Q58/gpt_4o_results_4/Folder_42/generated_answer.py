import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    target_number = 193
    for r in range(rows):
        for c in range(cols):
            for sub_rows in range(1, rows - r + 1):
                for sub_cols in range(1, cols - c + 1):
                    submatrix = matrix[r:r + sub_rows, c:c + sub_cols]
                    if np.size(submatrix) == target_number:
                        count += 1
    return count