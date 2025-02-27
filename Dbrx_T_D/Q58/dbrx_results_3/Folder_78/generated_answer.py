import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 < rows and j + 3 < cols and (np.count_nonzero(matrix[i:i + 3, j:j + 3] == 91) == 9):
                submatrix_count += 1
    return submatrix_count