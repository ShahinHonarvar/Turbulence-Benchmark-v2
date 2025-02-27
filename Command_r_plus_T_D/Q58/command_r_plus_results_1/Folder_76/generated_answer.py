import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_size = 159
    submatrix_rows = submatrix_cols = int(submatrix_size ** 0.5)
    count = 0
    for i in range(rows - submatrix_rows + 1):
        for j in range(cols - submatrix_cols + 1):
            submatrix = matrix[i:i + submatrix_rows, j:j + submatrix_cols]
            if submatrix.size == submatrix_size:
                count += 1
    return count