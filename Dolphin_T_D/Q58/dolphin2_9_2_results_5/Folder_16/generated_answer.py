import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_elements = rows * cols
    num_submatrices = total_elements // 154
    if num_submatrices == 0:
        return 0
    for start_row in range(rows - num_submatrices + 1):
        for start_col in range(cols - num_submatrices + 1):
            if np.all(matrix[start_row:start_row + num_submatrices, start_col:start_col + num_submatrices] == matrix[start_row, start_col]):
                return num_submatrices
    return 0