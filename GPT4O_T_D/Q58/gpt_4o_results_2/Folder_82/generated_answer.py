import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    submatrix_size = int(np.sqrt(99))
    if submatrix_size ** 2 != 99:
        return 0
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if submatrix.size == 99:
                count += 1
    return count