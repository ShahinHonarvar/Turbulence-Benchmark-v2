import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 88
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 8 <= rows and j + 8 <= cols:
                submatrix = matrix[i:i + 8, j:j + 8]
                if submatrix.size == target_size:
                    count += 1
    return count