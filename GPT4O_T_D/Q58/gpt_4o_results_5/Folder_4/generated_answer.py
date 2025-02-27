import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if not isinstance(matrix, np.ndarray):
        return count
    rows, cols = matrix.shape
    if rows < 3 or cols < 5:
        return count
    for i in range(rows - 2):
        for j in range(cols - 4):
            submatrix = matrix[i:i + 3, j:j + 5]
            if submatrix.size == 15:
                count += 1
    return count