import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_size = 179
    submatrix_rows = cols // submatrix_size
    submatrix_cols = rows // submatrix_size
    count = 0
    for i in range(submatrix_rows):
        for j in range(submatrix_cols):
            submatrix = matrix[i * submatrix_size:(i + 1) * submatrix_size, j * submatrix_size:(j + 1) * submatrix_size]
            if submatrix.size == submatrix_size ** 2:
                count += 1
    return count