import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 < rows and j + 3 < cols:
                submatrix = matrix[i:i + 4, j:j + 4]
                if submatrix.size == 16 and np.count_nonzero(submatrix) == 16:
                    submatrix_count += 1
    return submatrix_count