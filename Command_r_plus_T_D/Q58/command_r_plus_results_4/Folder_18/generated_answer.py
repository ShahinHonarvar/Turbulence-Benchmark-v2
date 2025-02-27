import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 104
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 10 <= rows and j + 10 <= cols:
                submatrix = matrix[i:i + 10, j:j + 10]
                if submatrix.size == target_size:
                    count += 1
    return count