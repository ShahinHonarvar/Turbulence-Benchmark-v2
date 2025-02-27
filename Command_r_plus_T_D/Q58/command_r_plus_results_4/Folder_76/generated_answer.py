import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_size = 159
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) == submatrix_size:
                count += 1
            elif (i + 1) * (j + 1) > submatrix_size:
                break
    return count