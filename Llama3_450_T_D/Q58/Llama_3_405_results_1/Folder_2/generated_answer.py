import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 107
    for row in range(rows):
        for col in range(cols):
            submat_rows = min(rows - row, int(np.ceil(n / (cols - col))))
            for submat_row in range(1, submat_rows + 1):
                submat_cols = min(cols - col, int(np.ceil(n / submat_row)))
                for submat_col in range(1, submat_cols + 1):
                    if submat_row * submat_col == n:
                        submat = matrix[row:row + submat_row, col:col + submat_col]
                        if submat.size == n:
                            count += 1
    return count