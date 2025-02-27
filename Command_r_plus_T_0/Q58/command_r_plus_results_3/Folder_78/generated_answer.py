import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    n = 91
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 <= rows and j + 3 <= cols:
                submatrix = matrix[i:i + 3, j:j + 3]
                if submatrix.size == n:
                    count += 1
    return count