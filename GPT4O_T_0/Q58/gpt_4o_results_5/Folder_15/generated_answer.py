import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 2 or cols < 2:
        return 0
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            unique_numbers = np.unique(submatrix)
            if len(unique_numbers) == 2:
                count += 1
    return count