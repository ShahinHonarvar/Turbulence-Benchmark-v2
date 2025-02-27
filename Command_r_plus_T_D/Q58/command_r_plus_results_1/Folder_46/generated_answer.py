import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 144
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 3 < row_count and j + 3 < col_count:
                submatrix = matrix[i:i + 4, j:j + 4]
                if submatrix.size == target_size:
                    submatrix_count += 1
    return submatrix_count