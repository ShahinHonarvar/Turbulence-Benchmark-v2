import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 179
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 5 <= rows and j + 5 <= cols:
                submatrix = matrix[i:i + 5, j:j + 5]
                if submatrix.size == target_size:
                    count += 1
    return count