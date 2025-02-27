import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_13_elements(matrix, r, c):
        submatrices_count = 0
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row, r):
                    for end_col in range(start_col, c):
                        rows_cnt = end_row - start_row + 1
                        cols_cnt = end_col - start_col + 1
                        if rows_cnt * cols_cnt == 13:
                            submatrices_count += 1
        return submatrices_count
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    rows, cols = matrix.shape
    return count_submatrices_with_13_elements(matrix, rows, cols)