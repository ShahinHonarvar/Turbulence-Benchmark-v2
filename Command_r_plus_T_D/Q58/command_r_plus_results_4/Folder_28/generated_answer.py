import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 12):
        for j in range(cols - 12):
            submatrix = matrix[i:i + 13, j:j + 13]
            if np.count_nonzero(submatrix == 37) == 37:
                count += 1
    return count