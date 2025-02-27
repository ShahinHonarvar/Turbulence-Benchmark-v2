import numpy as np

def submatrix_with_n_numbers(matrix, n=45):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_len in range(1, rows - r + 1):
                for c_len in range(1, cols - c + 1):
                    submatrix = matrix[r:r + r_len, c:c + c_len]
                    if submatrix.size == n and np.all(submatrix == n):
                        count += 1
    return count