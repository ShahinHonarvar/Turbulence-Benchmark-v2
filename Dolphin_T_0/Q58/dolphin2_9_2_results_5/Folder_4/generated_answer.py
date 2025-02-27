import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    if rows * cols < 15:
        return 0
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if len(np.unique(sub_matrix)) == 15:
                count += 1
    return count