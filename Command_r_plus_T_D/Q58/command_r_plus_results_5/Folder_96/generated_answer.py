import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 4 and np.count_nonzero(submatrix == 20) == 4:
                submatrix_count += 1
    return submatrix_count