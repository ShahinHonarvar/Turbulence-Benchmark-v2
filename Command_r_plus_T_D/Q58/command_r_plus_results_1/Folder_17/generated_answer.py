import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            if row + 4 < row_count and col + 4 < col_count:
                submatrix = matrix[row:row + 4, col:col + 4]
                if submatrix.size == 16 and np.count_nonzero(submatrix) == 16:
                    submatrix_count += 1
    return submatrix_count