import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not matrix.any():
        return []
    num_rows, num_cols = matrix.shape
    submatrices_with_sum_66 = []
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_end in range(row_start, num_rows):
                for col_end in range(col_start, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == 66:
                        submatrices_with_sum_66.append(submatrix)
    return submatrices_with_sum_66