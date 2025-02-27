import numpy as np

def submatrix_with_n_numbers(matrix, number=1, count=1):
    rows, cols = matrix.shape
    total_submatrices = 0
    for r in range(rows):
        for c in range(cols):
            for r_len in range(1, rows - r + 1):
                for c_len in range(1, cols - c + 1):
                    submatrix = matrix[r:r + r_len, c:c + c_len]
                    if np.count_nonzero(submatrix == number) == count:
                        total_submatrices += 1
    return total_submatrices