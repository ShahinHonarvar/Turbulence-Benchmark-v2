import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 80
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 2 <= rows and j + 2 <= cols:
                submatrix = matrix[i:i + 2, j:j + 2]
                if submatrix.size == target_sum:
                    count += 1
    return count