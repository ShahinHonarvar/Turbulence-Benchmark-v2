import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 53:
                for size in range(2, min(rows - r + 1, cols - c + 1)):
                    submatrix = matrix[r:r + size, c:c + size]
                    if np.count_nonzero(submatrix) == size * size:
                        count += 1
    return count