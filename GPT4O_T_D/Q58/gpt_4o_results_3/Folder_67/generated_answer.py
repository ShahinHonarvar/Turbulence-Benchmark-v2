import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    total_rows, total_columns = matrix.shape
    count = 0
    for start_row in range(total_rows):
        for start_column in range(total_columns):
            for end_row in range(start_row, total_rows):
                for end_column in range(start_column, total_columns):
                    sub_matrix = matrix[start_row:end_row + 1, start_column:end_column + 1]
                    if sub_matrix.size == 43:
                        count += 1
    return count