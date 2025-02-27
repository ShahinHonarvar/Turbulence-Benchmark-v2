import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 186
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 6 <= rows and j + 6 <= cols:
                submatrix = matrix[i:i + 6, j:j + 6]
                if submatrix.size == target_size:
                    count += 1
    return count