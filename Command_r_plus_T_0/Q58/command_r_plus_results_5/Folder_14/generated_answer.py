import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 7):
        for j in range(cols - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if submatrix.size == 84 and np.all(submatrix == 84):
                count += 1
    return count